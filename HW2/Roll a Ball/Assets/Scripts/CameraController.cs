using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour {

    public GameObject player;
    private Vector3 offset;

    private void Start()
    {
        offset = transform.position - player.transform.position;
    }

    // Runs after regular Update()
    // This way we know absolutly that the player has moved already.
    void LateUpdate()
    {
        transform.position = player.transform.position + offset;
    }

}
