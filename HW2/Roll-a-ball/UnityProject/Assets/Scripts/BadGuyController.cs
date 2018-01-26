using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BadGuyController : MonoBehaviour {

	public GameObject playerRef;
	public float speed;

	private Vector3 dir;

	// Use this for initialization
	void Start () {
		dir = new Vector3 (Random.Range(-1.0f, 1.0f), 0, Random.Range(-1.0f, 1.0f));
		dir = dir.normalized;
	}
	
	// Update is called once per frame
	void Update () {

		if (Time.frameCount % 90 < 3) {
			dir = new Vector3 (Random.Range(-1.0f, 1.0f), 0, Random.Range(-1.0f, 1.0f));
			dir = dir.normalized;
		}

		this.transform.Translate (dir * speed);
		transform.rotation = Quaternion.Euler(0, 0, 0);
	}
}
