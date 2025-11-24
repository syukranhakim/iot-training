#include <WiFi.h>
#include <HTTPClient.h>

/* WiFi configuration */
const char* ssid = "buffalo";
const char* password = "delicious";

/* Server configuration */
String server_ip = "192.168.1.3";

void setup() {
  Serial.begin(9600); 

  WiFi.begin(ssid, password);
  Serial.println("Connecting");

  /* Wait until connected */
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.print("Connected to WiFi with IP Address: ");
  Serial.println(WiFi.localIP());
}


/* Dummy function to read sensor value */
double get_sensor_value() {
  return (double) random(1000, 10000) / 100.;
}


/* Function to send HTTP GET request */
void send_http_get() {

  /* Check if WiFi is disconnected */
  if(WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi disconnected");
    return;
  }

  Serial.println("Sending GET request");

  /* Create http object */
  HTTPClient http;
  String endpoint = "http://" + server_ip + "/sensor.php";

  /* Initialize http */
  http.begin(endpoint.c_str());

  /* Send HTTP GET request */
  int response_code = http.GET();

  /* Handle response */
  if (response_code > 0) {
    Serial.print("HTTP Response code: ");
    Serial.println(response_code);
    String response_body = http.getString();
    Serial.println(response_body);
  }
  else {
    Serial.print("Error code: ");
    Serial.println(response_code);
  }

  /* Free http object */
  http.end();
  Serial.println();
}


/* Function to send HTTP POST request */
void send_http_post() {

  /* Check if WiFi is disconnected */
  if(WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi disconnected");
    return;
  }

  Serial.println("Sending POST request");

  /* Get sensor value */
  double sensor_value = get_sensor_value();

  HTTPClient http;
  String endpoint = "http://" + server_ip + "/sensor.php";

  /* Initialize http */
  http.begin(endpoint.c_str());

  /* Set header to be JSON */
  http.addHeader("Content-Type", "application/json");

  /* Format payload in JSON */
  String payload = "{\"value\":\"" + String(sensor_value, 2) + "\"}";
  int response_code = http.POST(payload);

  /* Handle response */
  if (response_code > 0) {
    Serial.print("HTTP Response code: ");
    Serial.println(response_code);
    String response_body = http.getString();
    Serial.println(response_body);
  }
  else {
    Serial.print("Error code: ");
    Serial.println(response_code);
  }

  /* Free http object */
  http.end();
  Serial.println();
}


void loop() {
  send_http_get();
  delay(5000);
  send_http_post();
  delay(5000);
}
