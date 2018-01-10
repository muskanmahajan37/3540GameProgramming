using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeController : MonoBehaviour {

    public float cubeSpeed;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {

         
        // Left right control
        if (Input.GetKey(KeyCode.LeftArrow))
        {
            this.transform.Translate(new Vector3(-1 * cubeSpeed * (float)Time.deltaTime, 0, 0));
        }
        else if (Input.GetKey(KeyCode.RightArrow))
        {
            this.transform.Translate(new Vector3(cubeSpeed * (float)Time.deltaTime, 0, 0));
        }

        // Up down control
        if (Input.GetKey(KeyCode.UpArrow))
        {
            this.transform.position = new Vector3(transform.position.x,
                                                  (cubeSpeed * (float)Time.deltaTime) + this.transform.position.y,
                                                  transform.position.z);
        }
        else if (Input.GetKey(KeyCode.DownArrow))
        {
            //this.transform.position.Set(0, (-1 * cubeSpeed * (float)Time.deltaTime) + this.transform.position.y, 0);
            this.transform.position = new Vector3(transform.position.x,
                                                  (-1 * cubeSpeed * (float)Time.deltaTime) + this.transform.position.y,
                                                  transform.position.z);
        }

        // Make the cube spin
        this.transform.Rotate(new Vector3(1, 0, 0));

        // Change the color
        this.GetComponent<Renderer>().material.color = new Color(255, 255, 255);
    }
}
