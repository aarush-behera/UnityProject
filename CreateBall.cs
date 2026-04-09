using UnityEngine;

public class CreateBall : MonoBehaviour
{
    public GameObject[] ball;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        int randominterval = Random.Range(3, 5);
        InvokeRepeating("SpawnBallRandom", 2, randominterval);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void SpawnBallRandom()
    {
        int randomball = Random.Range(0, ball.Length);
        int balldrop = Random.Range(-20, 5);

        Instantiate(ball[randomball], new Vector3(balldrop, 26, -4), ball[randomball].transform.rotation);

    }


}
