# https://slugs.do-api.dev/
# https://www.youtube.com/playlist?list=PL9evZl_m5wqsc7C38L9grx-djts2bqT_b

terraform {
  required_version = "~> 1.7.5"

  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }

    namecheap = {
      source = "namecheap/namecheap"
      version = ">= 2.0.0"
    }
    
  }
}

variable "do_token" {}
variable "nc_api_key" {}
variable "nc_user" { default = "acatejr" }

provider "digitalocean" {
  token = var.do_token
}

# provider "namecheap" {
#   user_name = var.nc_user
#   api_user = var.nc_user
#   api_key = var.nc_api_key
#   use_sandbox = false
# }

resource "digitalocean_ssh_key" "dada-forest" {
  name       = "Droplet ssh key"
  public_key = file("${path.module}/files/id_rsa.pub")
}

resource "digitalocean_droplet" "dada-forest" {
  image      = "ubuntu-23-10-x64"
  name       = "dada-forest"
  region     = "sfo3"
  size       = "s-1vcpu-1gb"
  monitoring = true
  ssh_keys = [
    digitalocean_ssh_key.dada-forest.id
  ]
  user_data = file("cloud-init.sh")
  tags      = ["dada-forest"]
}

# resource "namecheap_domain_records" "dada-forest-net" {
#   domain = "dadaforest.net"
#   mode = "OVERWRITE"

#   record {
#     hostname = "@" # This could also be something like "test" as test.dadaforest.net
#     type = "A"
#     address = digitalocean_droplet.dada-forest.ipv4_address
#   }
# }