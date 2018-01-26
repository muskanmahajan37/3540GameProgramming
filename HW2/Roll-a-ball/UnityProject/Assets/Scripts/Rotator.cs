using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotator : MonoBehaviour {
	
    public float rotateSpeed;

	// Update is called once per frame
	void Update () {
        this.GetComponent<Transform>().Rotate(
            new Vector3(rotateSpeed * 15, rotateSpeed * 30, rotateSpeed * 45) * Time.deltaTime);
	}
}
