using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AABBGizmo : MonoBehaviour
{
    void OnDrawGizmos()
    {
        drawAABB(this.transform.gameObject);
    }

    // Draw the axis aligned bounding box for the given object, all of the 
    // child objects, and the boxes around each sub tree.
    List<Vector3> drawAABB(GameObject obj)
    {
        // Base case, no children => draw a simple wire cube
        Renderer rend = obj.GetComponent<Renderer>();
        if (obj.transform.childCount == 0 && rend != null)
        {
            Gizmos.DrawWireCube(rend.bounds.center,
                                rend.bounds.size);
            List<Vector3> result2 = new List<Vector3>(2);
            result2.Add(rend.bounds.max);
            result2.Add(rend.bounds.min);
            return result2;
        }

        // Else there are children

        float xMin = float.MaxValue;
        float yMin = float.MaxValue;
        float zMin = float.MaxValue;
        float xMax = float.MinValue;
        float yMax = float.MinValue;
        float zMax = float.MinValue;

        // Get the children's min and max values in their aabb's
        // TODO: could increase efficency if we compared min/ max values
        //       as we recieve them instead of storing them all, then filtering...
        List<Vector3> childAABBs = new List<Vector3>();
        for (int i = 0; i < obj.transform.childCount; i++)
        {
            childAABBs.AddRange(drawAABB(obj.transform.GetChild(i).gameObject));
        }

        // Find the smallest and largest values for x, y, z
        foreach (Vector3 childSize in childAABBs)
        {
            xMin = Mathf.Min(xMin, childSize.x);
            yMin = Mathf.Min(yMin, childSize.y);
            zMin = Mathf.Min(zMin, childSize.z);

            xMax = Mathf.Max(xMax, childSize.x);
            yMax = Mathf.Max(yMax, childSize.y);
            zMax = Mathf.Max(zMax, childSize.z);
        }

        // Calculate side length
        float xSide = (xMax - xMin);
        float ySide = (yMax - yMin);
        float zSide = (zMax - zMin);

        // Calculate center of AABB
        float xCenter = (xSide / 2) + xMin;
        float yCenter = (ySide / 2) + yMin;
        float zCenter = (zSide / 2) + zMin;

        // Draw aabb
        Gizmos.DrawWireCube(new Vector3(xCenter, yCenter, zCenter),
                            new Vector3(xSide, ySide, zSide));

        // Package relevent min/ max values and return them 
        List<Vector3> result = new List<Vector3>(2);
        result.Add(new Vector3(xMin, yMin, zMin));
        result.Add(new Vector3(xMax, yMax, zMax));
        return result;
    }
}
