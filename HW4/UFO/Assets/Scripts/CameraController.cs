using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour {

    public GameObject player;
    private Vector3 offset;

    private void Start()
    {
        this.offset = this.transform.position - player.transform.position;
    }

    private void LateUpdate()
    {
        this.transform.position = player.transform.position + offset;
    }

}
