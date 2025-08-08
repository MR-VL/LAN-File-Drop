package main

const (
	uploadFolder = "./FileDrop"
	staticFolder = "./static"
	startPort    = 5000
)

var allowedExtensions = map[string]bool{
	".7z":   true,
	".gif":  true,
	".gz":   true,
	".jpeg": true,
	".jpg":  true,
	".m4a":  true,
	".mov":  true,
	".mp3":  true,
	".mp4":  true,
	".pdf":  true,
	".png":  true,
	".rar":  true,
	".tar":  true,
	".txt":  true,
	".wav":  true,
	".zip":  true,
}

func main() {

}
