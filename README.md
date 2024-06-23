# pyBird

pyBird is a simple API endpoint that rely on https://github.com/Imageomics/pybioclip to call [BioCLIP](https://imageomics.github.io/bioclip/)

## How to setup python
 - cf. [dedicated readme](./PYTHON_SETUP.md)

## How to run locally

Requirement : python

Command line only
````bash
make localTry
````
Note: the very-first time, hugging face cache is provisioned with openclip data `~/.cache/huggingface` (1.5GB)

Local flask server and http invoke
````bash
make localStart
# and in another terminal
make localCall
````
- to call API, you could also rely on Intellij httpClient [predict.http](./httpClient/predict.http)


## How to "secure" the endpoint

You could exige a private key in header by having `PYBIRD_PRIVATE_KEY` set on server side.
In that usecase, client must provide a `PRIVATE-KEY` with same value to avoid `403`

When no `PYBIRD_PRIVATE_KEY` is set, there is no security check.