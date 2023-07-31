
float ultrasonic_distance(int trigPin, int echoPin)

{

    long distance, duration;



    digitalWrite(trigPin, LOW);

    digitalWrite(echoPin, LOW);

    delayMicroseconds(2);



    digitalWrite(trigPin, HIGH);

    delayMicroseconds(10);

    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);

    distance = ((float)(340 * duration) / 1000) / 2;



    return distance;

}



int potentiometer_Read(int pin)

{

    int value;



    value = analogRead(pin) / 4;



    return value;

}



void motor_forward(int IN1, int IN2, int speed)

{

    analogWrite(IN1, speed);

    analogWrite(IN2, LOW);

}



void motor_backward(int IN1, int IN2, int speed)

{

    analogWrite(IN1, LOW);

    analogWrite(IN2, speed);

}



void motor_hold(int IN1, int IN2)

{

    analogWrite(IN1, LOW);

    analogWrite(IN2, LOW);

}


int handleA = 13;
int handleB = 12;
int leftA = 11;
int leftB = 10;
int rightA = 9;
int rightB = 8;

void setup(){
  Serial.begin(9600);
  pinMode(handleA , OUTPUT);
  pinMode(handleB , OUTPUT);
  pinMode(leftA , OUTPUT);
  pinMode(leftB , OUTPUT);
  pinMode(rightA , OUTPUT);
  pinMode(rightB , OUTPUT);
}

void loop(){
  Serial.println("Motor Forward");
  motor_forward(rightA, rightB, 175);
}

