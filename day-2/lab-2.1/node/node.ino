
#include <WiFiEspAT.h>
#include <SoftwareSerial.h>

/* Set DIO Pin 2 to be Arduino RX
 * Set DIO Pin 4 to be Arduino TX
 */
SoftwareSerial espSerial(2, 4);  

const char* server = "";

WiFiClient wifiClient;

/* Function to create HTTP POST request to server */
void send_http_post(int device, float value) {

  String postData = "device=" + String(device) + "&value=" + String(value, 2);

  if (!wifiClient.connect(server, 80)) {
    Serial.println("Failed to connect to server");
    return;
  }

  /* Raw HTTP POST request */
  wifiClient.println("POST /demo/update.php HTTP/1.1");
  wifiClient.println("Host: " + String(server));
  wifiClient.println("Content-Type: application/x-www-form-urlencoded");
  wifiClient.println("Content-Length: " + String(postData.length()));
  wifiClient.println("Connection: close");
  wifiClient.println();
  wifiClient.print(postData);
  Serial.println("Posted: " + postData);

  /* Clean response */
  while (wifiClient.available()) {
    Serial.print(wifiClient.read());
  }
}


void setup() {
    
  Serial.begin(9600);
  Serial.println("Booting...");

  /* Wait for ESP module to be ready */
  delay(5000);

  /* Init serial connection to ESP01s*/
  espSerial.begin(9600);
  Serial.println("Initiating WiFi Connection");

  /* Connect to WiFi */
  WiFi.init(espSerial);
  //WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
      Serial.print(".");
      delay(500);
  }

  Serial.println("WiFi Connected!");

  /* Check device IP address */
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  /* Ping server to check connection */
  Serial.println("Pinging server...");
  int result = WiFi.ping(server);
  Serial.println("Result: " + String(result));
}

void loop() {

  /* Define what value to send */
  float value = random(0, 10000) / 100.0;
  int device = 7;  // Change this to your group number

  /* Send data to server */
  send_http_post(device, value);

  /* Wait 5 seconds before next request */
  delay(5000);
}
