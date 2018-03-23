using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class navagate : MonoBehaviour {

    NavMeshAgent agent;
    Camera cam;

	// Use this for initialization
	void Start () {
        this.cam = Camera.main;
        this.agent = this.GetComponent<NavMeshAgent>();
	}
	
	// Update is called once per frame
	void Update () {
        if (Input.GetMouseButtonDown(0))
        {
            RaycastHit hit;
            Ray r = Camera.main.ScreenPointToRay(Input.mousePosition);
            Physics.Raycast(r, out hit);


            if (hit.collider.tag == "Terrain")
            {
                this.agent.destination = hit.point;
            }


        }
		
	}
}
