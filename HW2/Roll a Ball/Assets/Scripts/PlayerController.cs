using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour {

    public float ballSpeed;
    public Text countText;
    public Text winText;
    public Text clockText;

    private Rigidbody rb;
    private int count;
    private bool inAir;
    private bool gameStart;
    private float totalTimePlayed;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        count = 0;
        this.setCountText();
        winText.text = "";
        inAir = false;
        clockText.text = "0:00";
        gameStart = false;
        totalTimePlayed = 0.0f;
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space) && !inAir)
        {
            rb.AddForce(new Vector3(0.0f, 250, 0.0f));
            inAir = true;
        }

        if (gameStart)
        {
            totalTimePlayed += Time.deltaTime;
            int seconds = ((int)totalTimePlayed) % 60;
            int minutes = (int)(totalTimePlayed / 60);
            string textForClock = minutes.ToString() + ":";
            if (seconds < 10)
            {
                textForClock += "0" + seconds.ToString();
            } else
            {
                textForClock += seconds.ToString();
            }
            clockText.text = textForClock;
        }
    }

    void FixedUpdate()
    {
        if (Input.anyKeyDown)
        {
            gameStart = true;
        }

        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");

        rb.AddForce(new Vector3(moveHorizontal, 0.0f, moveVertical) * ballSpeed);
    }

    

    // Called when this player is about to touch an other collider
    void OnTriggerEnter(Collider other)
    {

    }

    void OnCollisionEnter(Collision collision)
    {
        // If we're back on the ground
        if (collision.gameObject.CompareTag("Ground"))
        {
            inAir = false;
        }

        // If we collide with a pickup.
        if (collision.gameObject.CompareTag("Pickup"))
        {
            collision.gameObject.SetActive(false);
            count++;
            this.setCountText();
        }
    }

    private void setCountText()
    {
        countText.text = "Count: " + count.ToString();
        if (count >= 8)
        {
            winText.text = "You win!";
            gameStart = false;
        }
    }
}
