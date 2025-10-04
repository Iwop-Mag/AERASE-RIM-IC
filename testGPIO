#include <wiringPi.h>
#include <iostream>
#include <unistd.h>

#define LED_PIN 0 // WiringPi pin 0 (Physical pin 11, GPIO 17)

int main() {
    // Initialize wiringPi
    if (wiringPiSetup() == -1) {
        std::cerr << "Failed to initialize wiringPi\n";
        return 1;
    }

    pinMode(LED_PIN, OUTPUT);

    std::cout << "Blinking LED on GPIO 17 (WiringPi pin 0)...\n";
    for (int i = 0; i < 10; ++i) {
        digitalWrite(LED_PIN, HIGH); // LED ON
        usleep(500000);              // 0.5 seconds
        digitalWrite(LED_PIN, LOW);  // LED OFF
        usleep(500000);              // 0.5 seconds
    }

    std::cout << "Done.\n";
    return 0;
}