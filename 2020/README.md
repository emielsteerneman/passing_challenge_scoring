# RoboCup 2020 SSL Technical Challenge Rules

Currently, one technical challenge is planned for the RoboCup 2020
competition. This challenge will be an extension of the 2019 SSL
Vision Blackout challenge.

Note: These rules are under development and subject to heavy
changes. You can use them as an idea to begin brainstorming but do not
be surprised if they are modified prior to official release.

## Building

The rules are written in asciidoc format.

### Using AsciiDoctor natively
Install AsciiDoctor on your system (https://asciidoctor.org/). Afterwards, build HTML5 version with
```
# Build the HTML5 version
asciidoctor 2020-ssl-vision-blackout-rules.adoc
# Build the PDF version
asciidoctor-pdf 2020-ssl-vision-blackout-rules.adoc
```

### Using docker image
If you have Docker installed, you can use the official AsciiDoctor image:
```
# Pull image once
docker pull asciidoctor/docker-asciidoctor
# Build the HTML5 version
docker run -v $PWD:/documents/ asciidoctor/docker-asciidoctor asciidoctor 2020-ssl-vision-blackout-rules.adoc
# Build the PDF version
docker run -v $PWD:/documents/ asciidoctor/docker-asciidoctor asciidoctor-pdf 2020-ssl-vision-blackout-rules.adoc
```
