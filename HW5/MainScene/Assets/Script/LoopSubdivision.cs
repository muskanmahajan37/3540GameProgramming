using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LoopSubdivision : MonoBehaviour
{
	class MeshHelper {
		public Vector3[] vertices;
		public int[] triangles;
	}

	private MeshHelper mesh1;
	private MeshHelper mesh2;
	private MeshHelper mesh3;
	private MeshHelper mesh4;

    private List<List<Vector3>> simpleTriangles;
    private Dictionary<int, float> lambdaOldWork;

    bool compareVertices(Vector3 v1, Vector3 v2) {
        return Mathf.Approximately(v1.x, v2.x) &&
               Mathf.Approximately(v1.y, v2.y) &&
               Mathf.Approximately(v1.z, v2.z);
    }

    bool inList(Vector3 v, List<Vector3> l) {
        foreach (Vector3 lv in l) {
            if(compareVertices(lv, v)) {
                return true;
            }
        }
        return false;
    }

    List<Vector3> findOldNeighbors(Vector3 p, List<List<Vector3>> triangles) {

        // Find every triangle that contains point p
        // Take all of their points, and add it to the master list
        List<Vector3> duplicateNeighbors = new List<Vector3>(12);
        foreach (List<Vector3> t in triangles) {
            if (compareVertices(t[0], p)) {
                duplicateNeighbors.Add(t[1]);
                duplicateNeighbors.Add(t[2]);
            }
            else if (compareVertices(t[1], p)) {
                duplicateNeighbors.Add(t[0]);
                duplicateNeighbors.Add(t[2]);
            }
            else if (compareVertices(t[2], p)) {
                duplicateNeighbors.Add(t[0]);
                duplicateNeighbors.Add(t[1]);
                
            }
        }

        // Remove duplicates from list of neighbors
        List<Vector3> result = new List<Vector3>(6);
        foreach(Vector3 n in duplicateNeighbors) {
            if (!inList(n, result)) { // If n is not in the list
                result.Add(n);
            } 
        }

        return result;
    }


    private Vector3 findTriangleOtherV(Vector3 e1, Vector3 e2, Vector3 bad, List<List<Vector3>> triangles) {
        // Loop through all the triangles, finding something that shares
        // e1, e2 but not bad

        bool containsE1 = false;
        bool containsE2 = false;
        bool containsBad = false;

        foreach(List<Vector3> t in triangles) {
            // does t contain e1 && e1 && NOT bad



            containsE1 = false;
            containsE2 = false;
            containsBad = false;

            foreach(Vector3 vert in t) {
                containsE1 = containsE1 || compareVertices(e1, vert);
                containsE2 = containsE2 || compareVertices(e2, vert);
                containsBad = containsBad || compareVertices(bad, vert);
            }



            if(containsE1 && containsE2 && (!containsBad)) {
                // Find the odd vertex out and return it
                    if (!(compareVertices(t[0], e1) || compareVertices(t[0], e2))) {
                    // If t[0] is not equal to e1 or e2
                    return t[0];
                } 
                else if(!(compareVertices(t[1], e1) || compareVertices(t[1], e2))) 
                {
                    // If t[1] is not equal to e1 or e2
                    return t[1];
                }
                else if (!(compareVertices(t[2], e1) || compareVertices(t[2], e2)))
                {
                    // If t[1] is not equal to e1 or e2
                    return t[2];
                }

            }
        }



        print("NOCAB Error in findTriangleOtherV triangles.count: " + triangles.Count);
        foreach (List<Vector3> lv in triangles) {
            print("  " + lv[0]);
            print("  " + lv[1]); 
            print("  " + lv[2]);
            print("----------------"); 
        }
        print("containsE1:  " + containsE1);
        print("containsE2:  " + containsE2);
        print("containsBad: " + containsBad);
        return new Vector3(0, 0, 0); // THis should never run
    }

    List<List<Vector3>> findEdgeNeighbors(Vector3 v1, Vector3 v2, Vector3 v3) {

        List<List<Vector3>> result = new List<List<Vector3>>(3);

        foreach(List<Vector3> t in this.simpleTriangles) {
            bool share0 = compareVertices(t[0], v1) ||
                          compareVertices(t[0], v2) ||
                          compareVertices(t[0], v3);
            bool share1 = compareVertices(t[1], v1) ||
                          compareVertices(t[1], v2) ||
                          compareVertices(t[1], v3);
            bool share2 = compareVertices(t[2], v1) ||
                          compareVertices(t[2], v2) ||
                          compareVertices(t[2], v3);

            // does the triangle share 2/3 of the vertices with provided triangle
            bool edgeNeighbor = ((share0 && share1 ) ||
                                 (share0 && share2) ||
                                 (share1 && share2));

            if (edgeNeighbor) {
                result.Add(t);
            }
        }

        return result;
    }

    float getLambda(int n) {

        if (this.lambdaOldWork.ContainsKey(n)) {
            return this.lambdaOldWork[n];
        }


        float result = (1.0f / n) * ((5.0f / 8.0f) -
                                         ((3.0f / 8.0f) +
                                           ((1.0f / 4.0f) *
                                            Mathf.Pow(Mathf.Cos((2.0f * Mathf.PI) / n), 2.0f))
                                          )
                                        );
        this.lambdaOldWork[n] = result;
        return result;
    }


	MeshHelper LoopSubdivide(MeshHelper mesh)
	{
		MeshHelper newMesh = new MeshHelper ();

        // TODO: implement Loop subdivision of mesh here

        Vector3 oldVertex1;
        Vector3 oldVertex2;
        Vector3 oldVertex3;

        Vector3 newVertex1;
        Vector3 newVertex2;
        Vector3 newVertex3;

        // Set up global vars
        this.simpleTriangles = new List<List<Vector3>>(mesh.triangles.Length / 3);
        if(this.lambdaOldWork == null) {
            this.lambdaOldWork = new Dictionary<int, float>();
        }

        //print("mesh.triangles.len :" + mesh.triangles.Length);
        for (int triangleNo = 0;
             triangleNo < mesh.triangles.Length;
             triangleNo += 3)
        {
            //print("triangleNO: " + triangleNo); 
            simpleTriangles.Add(
                new List<Vector3>(3) { mesh.vertices[mesh.triangles[triangleNo + 0]],
                                       mesh.vertices[mesh.triangles[triangleNo + 1]],
                                       mesh.vertices[mesh.triangles[triangleNo + 2]]});

        }


        List<Vector3> masterVertices = new List<Vector3>(mesh.vertices.Length);
        List<int> masterTriangles = new List<int>(mesh.triangles.Length * 4);

        foreach (List<Vector3> triangle in simpleTriangles)
        { // For every triangle

            // every triangle has 3 points
            Vector3 vertex1 = triangle[0];
            Vector3 vertex2 = triangle[1];
            Vector3 vertex3 = triangle[2];

            // any 2 of those points will make an edge => 3 edges

            // Find all triangles that are sharing this triangles edge
            List<List<Vector3>> edgeSharers = findEdgeNeighbors(vertex1, vertex2, vertex3);



            //Calculate the new midpoint along each edge
            float e = (1.0f / 8.0f);
            Vector3 up = vertex1;
            Vector3 left = vertex2;
            Vector3 right = vertex3;
            Vector3 down= findTriangleOtherV(vertex2, vertex3, vertex1, edgeSharers); 
            newVertex1 = (e * up) + (3.0f * e * left) + (3.0f * e * right) + (e * down);

            up = vertex3;
            left = vertex1;
            right = vertex2;
            down = findTriangleOtherV(vertex1, vertex2, vertex3, edgeSharers); // edge, edge, away
            newVertex2 = (e * up) + (3.0f * e * left) + (3.0f * e * right) + (e * down);


            up = vertex2;
            left = vertex3;
            right = vertex1;
            down = findTriangleOtherV(vertex1, vertex3, vertex2, edgeSharers);  // edge, edge, away
            newVertex3 = (e * up) + (3.0f * e * left) + (3.0f * e * right) + (e * down);



            // Now, update the old points

            // Every point has 6 triangles associated with it, and 6 old 
            // neighbor points. We need those points. 
            List<Vector3> oldNeighborsV1 = findOldNeighbors(vertex1, simpleTriangles);  // Returns a list of len 6
            List<Vector3> oldNeighborsV2 = findOldNeighbors(vertex2, simpleTriangles);
            List<Vector3> oldNeighborsV3 = findOldNeighbors(vertex3, simpleTriangles);

            int n = oldNeighborsV1.Count;
            float lambda = getLambda(n);
            Vector3 neighborSum = new Vector3(0, 0, 0);
            foreach (Vector3 neighbor in oldNeighborsV1)
            {
                neighborSum += neighbor;
            }
            oldVertex1 = ((1.0f - (n * lambda)) * vertex1) + (lambda * neighborSum);



            n = oldNeighborsV2.Count;
            lambda = getLambda(n);
            neighborSum = new Vector3(0, 0, 0);
            foreach (Vector3 neighbor in oldNeighborsV2)
            {
                neighborSum += neighbor;
            }
            oldVertex2 = ((1.0f - (n * lambda)) * vertex2) + (lambda * neighborSum);



            n = oldNeighborsV3.Count;
            lambda = getLambda(n);
            neighborSum = new Vector3(0, 0, 0);
            foreach (Vector3 neighbor in oldNeighborsV3)
            {
                neighborSum += neighbor;
            }
            oldVertex3 = ((1.0f - (n * lambda)) * vertex3) + (lambda * neighborSum);



            // From this point on, use oldVertex1/2/3 and newVertex1/2/3
            /*        ^
             *        *                    [old1]
             *      /   \ 
             *     * --- *             [new1    new2]
             *    /  \ /  \ 
             *   * -- * -- *        [old2   new3   old3]
             */

            int indexOld1 = -1;
            int indexOld2 = -1;
            int indexOld3 = -1;
            int indexNew1 = -1;
            int indexNew2 = -1;
            int indexNew3 = -1;

            // Check if the vertice is alreay in the master list
            for (int i = 0; i < masterVertices.Count; i++) {
                Vector3 curVert = masterVertices[i];

                // Look for 'old vertices'
                if (compareVertices(oldVertex1, curVert))
                    indexOld1 = i;
                
                if (compareVertices(oldVertex2, curVert))
                    indexOld2 = i;
                
                if (compareVertices(oldVertex3, curVert))
                    indexOld3 = i;
                
                // Look for 'new vertices' that aren't really new...
                if (compareVertices(newVertex1, curVert))
                    indexNew1 = i;
                
                if (compareVertices(newVertex2, curVert))
                    indexNew2 = i;
                
                if (compareVertices(newVertex3, curVert))
                    indexNew3 = i;
            }

            // If we didn't already see a point on the master list, then add it
            // If we didn't see the old vertice in the master list, then add it
            if (indexOld1 < 0)
            {
                masterVertices.Add(oldVertex1);
                indexOld1 = masterVertices.Count - 1;
            }
            if (indexOld2 < 0)
            {
                masterVertices.Add(oldVertex2);
                indexOld2 = masterVertices.Count - 1;
            }
            if (indexOld3 < 0)
            {
                masterVertices.Add(oldVertex3);
                indexOld3 = masterVertices.Count - 1;
            }
            if (indexNew1 < 0)
            {
                masterVertices.Add(newVertex1);
                indexNew1 = masterVertices.Count - 1;
            }
            if (indexNew2 < 0)
            {
                masterVertices.Add(newVertex2);
                indexNew2 = masterVertices.Count - 1;
            }
            if (indexNew3 < 0)
            {
                masterVertices.Add(newVertex3);
                indexNew3 = masterVertices.Count - 1;
            }

            // Use the indexes to build the new triangles
            List<int> t1 = new List<int>(3) { indexOld1, indexNew2, indexNew3 };
            List<int> t2 = new List<int>(3) { indexNew1, indexNew2, indexOld2 };
            List<int> t3 = new List<int>(3) { indexNew1, indexNew3, indexNew2 };
            List<int> t4 = new List<int>(3) { indexNew1, indexOld3, indexNew3 };

            // Add the new triangles to the master tri list
            masterTriangles.AddRange(t1);
            masterTriangles.AddRange(t2);
            masterTriangles.AddRange(t3);
            masterTriangles.AddRange(t4);
        }

        newMesh.vertices = masterVertices.ToArray();
        newMesh.triangles = masterTriangles.ToArray();

        // Clean up global vars
        this.simpleTriangles = new List<List<Vector3>>();
  
		//newMesh.triangles = (int[])mesh.triangles.Clone();
		//newMesh.vertices = (Vector3[])mesh.vertices.Clone();

		return newMesh;
	}

	void Start()
	{
		Mesh mesh = GetComponent<MeshFilter> ().mesh;

		mesh1 = new MeshHelper ();
		mesh1.vertices = mesh.vertices;
		mesh1.triangles = mesh.triangles;

		mesh2 = LoopSubdivide (mesh1);
        print("Mesh2 above ===============-======================= Mesh 3 below"); 
        mesh3 = LoopSubdivide (mesh2);
        print("Mesh3 above ======================================== Mesh 4 below"); 
		mesh4 = LoopSubdivide (mesh3);

		mesh.RecalculateNormals ();


        print("mesh1.vertices: " + mesh1.vertices);
        print("mesh1.vertices.len: " + mesh1.vertices.Length);

        print("mesh1.triangles: " + mesh1.triangles);
        print("mesh1.tri.len: " + mesh1.triangles.Length);

        print("-----------------------------------------"); 

        print("mesh2.vertices: " + mesh2.vertices);
        print("mesh2.vertices.len: " + mesh2.vertices.Length);

        print("mesh2.triangles: " + mesh2.triangles);
        print("mesh2.tri.len: " + mesh2.triangles.Length);

        print("-----------------------------------------");

        print("mesh3.vertices: " + mesh3.vertices);
        print("mesh3.vertices.len: " + mesh3.vertices.Length);

        print("mesh3.triangles: " + mesh3.triangles);
        print("mesh3.tri.len: " + mesh3.triangles.Length);

        print("-----------------------------------------");

        print("mesh4.vertices: " + mesh4.vertices);
        print("mesh4.vertices.len: " + mesh4.vertices.Length);

        print("mesh4.triangles: " + mesh4.triangles);
        print("mesh4.tri.len: " + mesh4.triangles.Length);

	}

	void Update ()
	{
		if (Input.GetKeyDown (KeyCode.Alpha1) || Input.GetKeyDown (KeyCode.Alpha2) || Input.GetKeyDown (KeyCode.Alpha3) || Input.GetKeyDown (KeyCode.Alpha4)) {
			Mesh mesh = GetComponent<MeshFilter> ().mesh;
			mesh.Clear ();

			if (Input.GetKeyDown (KeyCode.Alpha1)) {
				mesh.vertices = mesh1.vertices;
				mesh.triangles = mesh1.triangles;
			}
			if (Input.GetKeyDown (KeyCode.Alpha2)) {
				mesh.vertices = mesh2.vertices;
				mesh.triangles = mesh2.triangles;
			}
			if (Input.GetKeyDown (KeyCode.Alpha3)) {
				mesh.vertices = mesh3.vertices;
				mesh.triangles = mesh3.triangles;
			}
			if (Input.GetKeyDown (KeyCode.Alpha4)) {
				mesh.vertices = mesh4.vertices;
				mesh.triangles = mesh4.triangles;
			}

			mesh.RecalculateNormals ();
		}
	}
}
