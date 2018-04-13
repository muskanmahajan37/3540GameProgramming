using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GenerateTerrain : MonoBehaviour {


	Mesh mesh;
	int[,] verticesHelper;
	int timesUpdated = 0;

	// Use this for initialization
	void Start () {
    Vector3[] newVertices = new Vector3[81];
		this.verticesHelper = new int[9, 9]; // Given an x,y retrun an index in newVertices
    int[] newTriangles = new int[384]; // 128 * 3 = 384

		for (int y = 0; y < 9; y++) {
			for (int x = 0; x < 9; x++) {
				int index = (9 * y) + x;
				newVertices[index] = new Vector3(x, y, 0);
				verticesHelper[x, y] = index;
			}
		}

		int newTrianglesNextIndex = 0;
		// Generate the triangeles 1 square at a time  (8 triangles per inner loop)
		for (int yy = 0; yy < 4; yy++) {
			for (int xx = 0; xx < 4; xx++) {

				int x = xx * 2;
				int y = yy * 2;

				int tl = verticesHelper[x,   y];
				int tc = verticesHelper[x+1, y];
				int tr = verticesHelper[x+2, y];

				int l = verticesHelper[x,   y+1];
				int c = verticesHelper[x+1, y+1];
				int r = verticesHelper[x+2, y+1];

				int bl = verticesHelper[x,   y+2];
				int bc = verticesHelper[x+1, y+2];
				int br = verticesHelper[x+2, y+2];

				newTriangles[newTrianglesNextIndex++] = tl;
				newTriangles[newTrianglesNextIndex++] = c;
				newTriangles[newTrianglesNextIndex++] = l;

				newTriangles[newTrianglesNextIndex++] = tl;
				newTriangles[newTrianglesNextIndex++] = tc;
				newTriangles[newTrianglesNextIndex++] = c;

				newTriangles[newTrianglesNextIndex++] = tc;
				newTriangles[newTrianglesNextIndex++] = tr;
				newTriangles[newTrianglesNextIndex++] = c;

				newTriangles[newTrianglesNextIndex++] = c;
				newTriangles[newTrianglesNextIndex++] = tr;
				newTriangles[newTrianglesNextIndex++] = r;
				//////////////////////////////////////////////
				newTriangles[newTrianglesNextIndex++] = l;
				newTriangles[newTrianglesNextIndex++] = c;
				newTriangles[newTrianglesNextIndex++] = bl;

				newTriangles[newTrianglesNextIndex++] = bl;
				newTriangles[newTrianglesNextIndex++] = c;
				newTriangles[newTrianglesNextIndex++] = bc;

				newTriangles[newTrianglesNextIndex++] = c;
				newTriangles[newTrianglesNextIndex++] = br;
				newTriangles[newTrianglesNextIndex++] = bc;

				newTriangles[newTrianglesNextIndex++] = c;
				newTriangles[newTrianglesNextIndex++] = r;
				newTriangles[newTrianglesNextIndex++] = br;
			}
		}

    Mesh mesh = new Mesh();
    this.GetComponent<MeshFilter>().mesh = mesh;
		this.mesh = mesh;
		mesh.vertices = newVertices;
    mesh.triangles = newTriangles;

	}

	// Update is called once per frame
	void Update () {

		if (Input.GetKeyDown(KeyCode.Space)) {

			if (timesUpdated < 7) {
				showOff();
			}else {
				generateTerrain();
			}
			this.timesUpdated += 1;
		}

	}

	void generateTerrain() {
		Vector3[] newVertices = this.mesh.vertices;
		int[] newTriangles = this.mesh.triangles; // 128 * 3 = 384


		List<int> squares = new List<int>(); // A list of the corners of the newest squares
																				 // Each element is an index from verticesHelper

		// Initialize corrner values
		int tempIndex = this.verticesHelper[0, 0];
		newVertices[tempIndex].z = Random.Range( 0.0f, 1.0f );
		squares.Add(tempIndex);

		tempIndex = this.verticesHelper[8, 0];
		newVertices[tempIndex].z =  Random.Range( 0.0f, 1.0f );
		squares.Add(tempIndex);

		tempIndex = this.verticesHelper[8, 8];
		newVertices[tempIndex].z =  Random.Range( 0.0f, 1.0f );
		squares.Add(tempIndex);

		tempIndex = this.verticesHelper[0, 8];
		newVertices[tempIndex].z =  Random.Range( 0.0f, 1.0f );
		squares.Add(tempIndex);

		for (int i = 0 ; i < 8; i ++) {

			// dimond step => find center
			print(squares.Count / 4);
			for (int jj = 0; jj < (squares.Count / 4); jj++) {

				int tlIndex = squares[(jj * 4) + 0]; // an index to be looked up in newVertices
				int trIndex = squares[(jj * 4) + 1];
				int brIndex = squares[(jj * 4) + 2];
				int blIndex = squares[(jj * 4) + 3];

				Vector3 tlVert = newVertices[tlIndex];
				Vector3 trVert = newVertices[trIndex];
				Vector3 brVert = newVertices[brIndex];
				Vector3 blVert = newVertices[blIndex];

				int centerVertX = ((int)(tlVert.x + brVert.x)) / 2;
				int centerVertY = ((int)(tlVert.y + brVert.y)) / 2;

				float average = (tlVert.z + trVert.z + brVert.z + blVert.z) / 4;
				float bump = Random.Range(-1.0f, 1.0f) / ((i * 3) + 1);

				int centerIndex = this.verticesHelper[centerVertX, centerVertY];
				newVertices[centerIndex].z = average + bump;
			}

			// square step => find edges
			int j = 0;
			int count = squares.Count/4;
			for (; j < count; j++) {
				int tlIndex = squares[(j * 4) + 0]; // an index to be looked up in newVertices
				int trIndex = squares[(j * 4) + 1];
				int brIndex = squares[(j * 4) + 2];
				int blIndex = squares[(j * 4) + 3];

				Vector3 tlVert = newVertices[tlIndex];
				Vector3 trVert = newVertices[trIndex];
				Vector3 brVert = newVertices[brIndex];
				Vector3 blVert = newVertices[blIndex];

				int centerVertX = ((int)(tlVert.x + brVert.x)) / 2;
				int centerVertY = ((int)(tlVert.y + brVert.y)) / 2;
				Vector3 cVert = newVertices[this.verticesHelper[centerVertX, centerVertY]];

				float average;
				float bump;

				// Find top center index
				int topCenterIndex = this.verticesHelper[centerVertX, (int)tlVert.y];
				average = (tlVert.z + cVert.z + trVert.z) / 3;
				bump = Random.Range(-1.0f, 1.0f) / ((i * 3) + 2);
				newVertices[topCenterIndex].z = average + bump;

				int rightCenterIndex = this.verticesHelper[(int)trVert.x, centerVertY];
				average = (trVert.z + cVert.z + brVert.z) / 3;
				bump = Random.Range(-1.0f, 1.0f) / ((i * 3) + 2);
				newVertices[rightCenterIndex].z = average + bump;

				int botCenterIndex = this.verticesHelper[centerVertX, (int)blVert.y];
				average = (blVert.z + cVert.z + brVert.z) / 3;
				bump = Random.Range(-1.0f , 1.0f) / ((i * 3) + 2);
				newVertices[botCenterIndex].z = average + bump;

				int leftCenterIndex = this.verticesHelper[(int)tlVert.x, centerVertY];
				average = (tlVert.z + blVert.z + cVert.z) / 3;
				bump = Random.Range(-1.0f, 1.0f) / ((i * 3) + 2);
				newVertices[leftCenterIndex].z = average + bump;

				// Might as well set the center on too for good measure
				int centerIndex = this.verticesHelper[centerVertX, centerVertY];
				//newVertices[centerIndex].z = 1;

				squares.Add(tlIndex);
				squares.Add(topCenterIndex);
				squares.Add(centerIndex);
				squares.Add(leftCenterIndex);

				squares.Add(topCenterIndex);
				squares.Add(trIndex);
				squares.Add(rightCenterIndex);
				squares.Add(centerIndex);

				squares.Add(centerIndex);
				squares.Add(rightCenterIndex);
				squares.Add(brIndex);
				squares.Add(botCenterIndex);

				squares.Add(leftCenterIndex);
				squares.Add(centerIndex);
				squares.Add(botCenterIndex);
				squares.Add(blIndex);
			}

			squares.RemoveRange(0, (j * 4));



		this.mesh.vertices = newVertices;
		}
	}

	void showOff() {
		Vector3[] newVertices = this.mesh.vertices;
		int[] newTriangles = this.mesh.triangles; // 128 * 3 = 384


		List<int> squares = new List<int>(); // A list of the corners of the newest squares
																				 // Each element is an index from verticesHelper

		// Initialize corrner values
		int tempIndex = this.verticesHelper[0, 0];
		newVertices[tempIndex].z = 1;
		squares.Add(tempIndex);

		tempIndex = this.verticesHelper[8, 0];
		newVertices[tempIndex].z = 1;
		squares.Add(tempIndex);

		tempIndex = this.verticesHelper[8, 8];
		newVertices[tempIndex].z = 1;
		squares.Add(tempIndex);

		tempIndex = this.verticesHelper[0, 8];
		newVertices[tempIndex].z = 1;
		squares.Add(tempIndex);

		for (int i = 0 ; i < this.timesUpdated; i ++) {

			if ((i % 2) == 0) {
				print("domond step");
				// dimond step => find center
				print(squares.Count / 4);
				for (int j = 0; j < (squares.Count / 4); j++) {
					print("j :" + j + "    squares.Count/4:" + (squares.Count / 4));

					int tlIndex = squares[(j * 4) + 0]; // an index to be looked up in newVertices
					int trIndex = squares[(j * 4) + 1];
					int brIndex = squares[(j * 4) + 2];
					int blIndex = squares[(j * 4) + 3];

					Vector3 tlVert = newVertices[tlIndex];
					Vector3 trVert = newVertices[trIndex];
					Vector3 brVert = newVertices[brIndex];
					Vector3 blVert = newVertices[blIndex];

					int centerVertX = ((int)(tlVert.x + brVert.x)) / 2;
					int centerVertY = ((int)(tlVert.y + brVert.y)) / 2;
					print("centerVertX: " + centerVertX + "   centerVertY: " + centerVertY);

					int centerIndex = this.verticesHelper[centerVertX, centerVertY];
					newVertices[centerIndex].z = 1;
				}
			}
			else
			{
				// square step => find edges
				int j = 0;
				int count = squares.Count/4;
				for (; j < count; j++) {
					print(j);
					int tlIndex = squares[(j * 4) + 0]; // an index to be looked up in newVertices
					int trIndex = squares[(j * 4) + 1];
					int brIndex = squares[(j * 4) + 2];
					int blIndex = squares[(j * 4) + 3];

					Vector3 tlVert = newVertices[tlIndex];
					Vector3 trVert = newVertices[trIndex];
					Vector3 brVert = newVertices[brIndex];
					Vector3 blVert = newVertices[blIndex];

					int centerVertX = ((int)(tlVert.x + brVert.x)) / 2;
					int centerVertY = ((int)(tlVert.y + brVert.y)) / 2;

					// Find top center index
					int topCenterIndex = this.verticesHelper[centerVertX, (int)tlVert.y];
					newVertices[topCenterIndex].z = 1;

					int rightCenterIndex = this.verticesHelper[(int)trVert.x, centerVertY];
					newVertices[rightCenterIndex].z = 1;

					int botCenterIndex = this.verticesHelper[centerVertX, (int)blVert.y];
					newVertices[botCenterIndex].z = 1;

					int leftCenterIndex = this.verticesHelper[(int)tlVert.x, centerVertY];
					newVertices[leftCenterIndex].z = 1;

					// Might as well set the center on too for good measure
					int centerIndex = this.verticesHelper[centerVertX, centerVertY];
					newVertices[centerIndex].z = 1;

					squares.Add(tlIndex);
					squares.Add(topCenterIndex);
					squares.Add(centerIndex);
					squares.Add(leftCenterIndex);

					squares.Add(topCenterIndex);
					squares.Add(trIndex);
					squares.Add(rightCenterIndex);
					squares.Add(centerIndex);

					squares.Add(centerIndex);
					squares.Add(rightCenterIndex);
					squares.Add(brIndex);
					squares.Add(botCenterIndex);

					squares.Add(leftCenterIndex);
					squares.Add(centerIndex);
					squares.Add(botCenterIndex);
					squares.Add(blIndex);
				}

				squares.RemoveRange(0, (j * 4));
			}
		}



		this.mesh.vertices = newVertices;
	}
}
