# RoboCup 2021 SSL Technical Challenge Rules

Currently, one technical challenge is planned for the RoboCup 2021 competition.
This challenge will be an extension of the 2019 SSL Vision Blackout challenge,
but adapted for the remote competition format.

## Building

The rules are written in asciidoc format.

### Using AsciiDoctor natively
Install AsciiDoctor on your system (https://asciidoctor.org/). Afterwards, build HTML5 version with
```
# Build the HTML5 version
asciidoctor 2021-ssl-vision-blackout-rules.adoc
# Build the PDF version
asciidoctor-pdf 2021-ssl-vision-blackout-rules.adoc
```

### Using docker image
If you have Docker installed, you can use the official AsciiDoctor image:
```
# Pull image once
docker pull asciidoctor/docker-asciidoctor
# Build the HTML5 version
docker run -v $PWD:/documents/ asciidoctor/docker-asciidoctor asciidoctor 2021-ssl-vision-blackout-rules.adoc
# Build the PDF version
docker run -v $PWD:/documents/ asciidoctor/docker-asciidoctor asciidoctor-pdf 2021-ssl-vision-blackout-rules.adoc
```
