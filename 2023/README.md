# RoboCup 2023 SSL Technical Challenge Rules

## Building

The rules are written in asciidoc format.

### Using AsciiDoctor natively

Install AsciiDoctor on your system (https://asciidoctor.org/). Afterwards,
build HTML5 version with

```
# Build the HTML5 version
asciidoctor 2023-ssl-ball-placement-rules.adoc
# Build the PDF version
asciidoctor-pdf 2023-ssl-ball-placement-rules.adoc
```

### Using docker image

If you have Docker installed, you can use the official AsciiDoctor image:

```
# Pull image once
docker pull asciidoctor/docker-asciidoctor
# Build the HTML5 version
docker run -v $PWD:/documents/ asciidoctor/docker-asciidoctor asciidoctor 2023-ssl-ball-placement-rules.adoc
# Build the PDF version
docker run -v $PWD:/documents/ asciidoctor/docker-asciidoctor asciidoctor-pdf 2023-ssl-ball-placement-rules.adoc
```
