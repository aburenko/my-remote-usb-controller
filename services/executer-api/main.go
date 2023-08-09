package main

import (
    "log"
    "os"
    "os/exec"
    "github.com/gin-gonic/gin"
)

func main() {
    r := gin.Default()

    // POST route to turn the device on
    r.POST("/on", func(c *gin.Context) {
        err := executeCommand("sudo uhubctl -l 2 -a on")
        if err != nil {
            c.JSON(500, gin.H{"error": "Failed to turn device on"})
            return
        }
        c.JSON(200, gin.H{"message": "Device is now ON"})
    })

    // POST route to turn the device off
    r.POST("/off", func(c *gin.Context) {
        err := executeCommand("sudo uhubctl -l 2 -a off")
        if err != nil {
            c.JSON(500, gin.H{"error": "Failed to turn device off"})
            return
        }
        c.JSON(200, gin.H{"message": "Device is now OFF"})
    })

    // Start the server
    if err := r.Run(":8888"); err != nil {
        log.Fatal(err)
    }
}

func executeCommand(command string) error {
    cmd := exec.Command(command)
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    return cmd.Run()
}


