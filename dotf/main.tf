# https://slugs.do-api.dev/
# https://www.youtube.com/playlist?list=PL9evZl_m5wqsc7C38L9grx-djts2bqT_b

terraform {
  required_version = "~> 1.7.5"

  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

provider "digitalocean" {}

resource "digitalocean_droplet" "data-forest" {
  image     = "ubuntu-23-10-x64"
  name      = "dada-forest"
  region    = "sfo3"
  size      = "s-1vcpu-1gb"
  # user_data = file("terramino_app.yaml")
  user_data = file("cloud-init.sh")
}