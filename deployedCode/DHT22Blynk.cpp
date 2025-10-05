// Minimal Blynk Linux example for Raspberry Pi
// Compile with: g++ blynk_linux.cpp -I ~/blynk-library/src -o blynk_linux
// Run with:    ./blynk_linux

#include <BlynkApiLinux.h>
#include <BlynkSocket.h>
#include <BlynkOptionsParser.h>

static BlynkTransportSocket _blynkTransport;
BlynkSocket Blynk(_blynkTransport);

void setup()
{
    // Example: write a value to Virtual Pin V0 when connected
    Blynk.virtualWrite(0, "Hello from Raspberry Pi!");
}

void loop()
{
    Blynk.run();
}

int main(int argc, char* argv[])
{
    const char* auth;
    // Parse options: ./blynk_linux --token=YOUR_DEVICE_AUTH_TOKEN
    parse_options(argc, argv, auth);

    Blynk.begin(auth);

    setup();
    while (true) {
        loop();
    }

    return 0;
}
