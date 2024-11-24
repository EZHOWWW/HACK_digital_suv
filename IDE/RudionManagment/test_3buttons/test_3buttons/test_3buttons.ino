#include "Arduino.h"

void setup()
{
        pinMode(BUTTON_BUILTIN_1, INPUT_PULLDOWN);
        pinMode(BUTTON_BUILTIN_2, INPUT_PULLDOWN);
        pinMode(BUTTON_BUILTIN_3, INPUT_PULLDOWN);
        pinMode(LED_BUILTIN_1, OUTPUT);
        pinMode(LED_BUILTIN_2, OUTPUT);
        digitalWrite(LED_BUILTIN_1, false);
        digitalWrite(LED_BUILTIN_2, false);
}

bool btnState;

void loop()
{       

        btnState = digitalRead(BUTTON_BUILTIN_2);
        if (btnState)
        {
                    digitalWrite(LED_BUILTIN_1, false);
                    digitalWrite(LED_BUILTIN_2, false);
        }
      
        btnState = digitalRead(BUTTON_BUILTIN_1);
        if (btnState)
        {
                digitalWrite(LED_BUILTIN_1, true);
        }
      
        btnState = digitalRead(BUTTON_BUILTIN_3);
        if (btnState)
        {
                digitalWrite(LED_BUILTIN_2, true);
        }
      
}