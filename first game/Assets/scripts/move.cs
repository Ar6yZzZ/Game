using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class move : MonoBehaviour
{
   private Rigidbody2D ball;
   public float speed, jumpImpulse; 
   void Start() {
       ball = GetComponent<Rigidbody2D>();
       speed *= 400;
   }
   private void Update() {
        if (Input.GetKeyDown(KeyCode.W)) { 
            ball.AddForce(Vector2.up * jumpImpulse, ForceMode2D.Impulse); 
        }
   }

   private void FixedUpdate() {
        if (Input.GetKey(KeyCode.A)) {
            ball.AddForce(Vector2.left * speed * Time.fixedDeltaTime);
        }
 
        if (Input.GetKey(KeyCode.D))
        {
            ball.AddForce(Vector2.right * speed * Time.fixedDeltaTime);
        }
   }
}
