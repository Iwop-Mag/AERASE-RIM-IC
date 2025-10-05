
#include <BlynkSimpleStream.h>
#include <wiringPi.h>

// Blynk authorization token
char auth[] = "YourAuthToken"; // Replace with your Blynk token

// GPIO pin for LED (using wiringPi pin numbering)
const int LED_PIN = 0; // GPIO17 (wiringPi pin 0)

void setup()
{
    wiringPiSetup();
    pinMode(LED_PIN, OUTPUT);
    Blynk.begin(auth, Serial);
}

// Blynk virtual pin handler (V1 button)
BLYNK_WRITE(V1)
{
    int ledState = param.asInt();
    digitalWrite(LED_PIN, ledState ? HIGH : LOW);
}

void loop()
{
    Blynk.run();
}

int main()
{
    setup();
    while (true)
    {
        loop();
        delay(10);
    }
    return 0;
}