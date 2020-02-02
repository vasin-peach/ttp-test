package main

import (
	"bufio"
	"encoding/json"
	"log"
	"net/http"
	"os"
)

func readTxt() []map[string]string {
	var txtlines []string
	logoList := []map[string]string{}

	file, err := os.Open("url.txt")

	if err != nil {
		log.Fatalf("failed opening file: %s", err)
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	// scan txt
	for scanner.Scan() {
		txtlines = append(txtlines, scanner.Text())
	}

	// loop each line to map
	for _, eachline := range txtlines {
		logoMap := make(map[string]string)
		logoMap["logo"] = eachline
		logoList = append(logoList, logoMap)
	}

	file.Close()
	return logoList
}

func getImageURL(w http.ResponseWriter, r *http.Request) {
	url := readTxt()
	data := make(map[string][]map[string]string)
	data["companies"] = url

	// map to json
	json.NewEncoder(w).Encode(data)
}

func handleRequest() {
	http.HandleFunc("/companies", getImageURL)
	http.ListenAndServe(":3000", nil) // listen at port 3000
}

func main() {
	handleRequest()
}
