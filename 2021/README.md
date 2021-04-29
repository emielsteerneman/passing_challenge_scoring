# RoboCup 2021 SSL Technical Challenge Rules

Currently, two technical challenges are planned for the RoboCup 2021
competition. The first challenge will be an extension of the 2019 SSL Vision
Blackout challenge. The second will be a autonomous ball placement challenge
for Divison B only teams.

Note: These rules are under development and subject to heavy
changes. You can use them as an idea to begin brainstorming but do not
be surprised if they are modified prior to official release.

## Building

The rules are written in asciidoc format.

### Using AsciiDoctor natively

Install AsciiDoctor on your system (https://asciidoctor.org/). Afterwards,
build HTML5 version with

```
# Build the HTML5 version
asciidoctor 2021-ssl-vision-blackout-rules.adoc
asciidoctor 2021-ssl-ball-placement-rules.adoc
# Build the PDF version
asciidoctor-pdf 2021-ssl-vision-blackout-rules.adoc
asciidoctor 2021-ssl-ball-placement-rules.adoc
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
