using UnityEngine;
using UnityEngine.Rendering;

public class DogForward : MonoBehaviour
{
    public float speed = 27.0f;
  
    void Start()
    {
        
    }

 
    void Update()
    {
        
        transform.Translate(Vector3.forward * Time.deltaTime *  speed);
    }
}
