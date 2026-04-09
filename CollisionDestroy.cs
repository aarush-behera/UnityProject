using UnityEngine;
using UnityEngine.SocialPlatforms.Impl;

public class CollisionDestroy : MonoBehaviour
{
    public float score = 0;
    public float floorBoundary = -3.0f;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnTriggerEnter(Collider other)
    {
        Destroy(gameObject);
    }

    
}
