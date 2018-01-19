using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveAway : MonoBehaviour {

    public GameObject playerRef;
    public float speed;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        Transform closestTransform = this.transform.GetChild(0);
        float currentClosestDist = 999.99f;
        foreach (Transform child in this.transform)
        {
            float distToChild = Vector3.Distance(playerRef.transform.position,
                                                 child.transform.position);
            if (distToChild < currentClosestDist)
            {
                currentClosestDist = distToChild;
                closestTransform = child.transform;
            }
        }

        // Find the direction to move in
        Vector3 yStrippedClosest = 
            new Vector3(closestTransform.transform.position.x,
                        0,
                        closestTransform.transform.position.z);
        Vector3 yStripedPlayer =
            new Vector3(playerRef.transform.position.x,
                        0,
                        playerRef.transform.position.z);
        Vector3 direction = yStrippedClosest - yStripedPlayer;

        // Normalize the vector
        direction.Normalize();

        // Apply the movement to the pickup
        closestTransform.transform.Translate(direction * speed, Space.World);
	}
}
