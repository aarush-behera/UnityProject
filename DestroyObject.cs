using UnityEngine;

public class DestroyObject : MonoBehaviour
{
    public float Boundary = -40.0f;
    public float floorBoundary = -3.0f;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(transform.position.x < Boundary)
        {
            Destroy(gameObject);
        }

        if(transform.position.y < floorBoundary)
        {
            Destroy(gameObject);
            Debug.Log("Game Over!");
        }
    }
}
