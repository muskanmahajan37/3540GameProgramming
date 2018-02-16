using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Controller : MonoBehaviour {

    private bool nextAnimation = false;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKeyDown(KeyCode.Space))
        {
            this.nextAnimation = !nextAnimation;
            this.GetComponent<Animator>().SetBool("NextAnimation", nextAnimation);
        }
	}
}
