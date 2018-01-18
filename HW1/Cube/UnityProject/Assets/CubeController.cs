using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeController : MonoBehaviour {

    public float cubeSpeed;
    public float cubeScaleSpeed;
    
    bool xRotate = true;
    bool yRotate = false;
    bool zRotate = false;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {

         
        // Left right control
        if (Input.GetKey(KeyCode.LeftArrow))
        {
            this.transform.position = new Vector3((-1 * cubeSpeed * (float)Time.deltaTime) +
                                                      this.transform.position.x,
                                                  transform.position.y,
                                                  transform.position.z);
        }
        else if (Input.GetKey(KeyCode.RightArrow))
        {
            this.transform.position = new Vector3((cubeSpeed * (float)Time.deltaTime) +
                                                        this.transform.position.x,
                                                  transform.position.y,
                                                  transform.position.z);
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
           this.transform.position = new Vector3(transform.position.x,
                                                  (-1 * cubeSpeed * (float)Time.deltaTime) + this.transform.position.y,
                                                  transform.position.z);
        }



        // Make the cube spin
        this.transform.Rotate(new Vector3(1,1,1));
        
        
        // Change the color to red
        this.GetComponent<Renderer>().material.SetColor("_Color", new Color(255, 0, 0));

        // Scale the shape 
        if (Input.GetKey(KeyCode.Q))
        {
            this.transform.localScale += 
                new Vector3(cubeScaleSpeed * (float)Time.deltaTime,
                            cubeScaleSpeed * (float)Time.deltaTime,
                            cubeScaleSpeed * (float)Time.deltaTime);
        }
        else if (Input.GetKey(KeyCode.W))
        {
            this.transform.localScale -=
                new Vector3(cubeScaleSpeed * (float)Time.deltaTime,
                            cubeScaleSpeed * (float)Time.deltaTime,
                            cubeScaleSpeed * (float)Time.deltaTime);
        }
    }
}
