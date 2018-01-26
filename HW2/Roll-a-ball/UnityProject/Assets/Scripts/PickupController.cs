using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PickupController : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        // We need to keep the pick up on the same y level the entire time
        Vector3 updatedPos = new Vector3(this.transform.position.x,
                                         0.95f,
                                         this.transform.position.z);
        this.transform.position = updatedPos;
	}
}
