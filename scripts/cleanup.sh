#!/bin/bash
docker stop mypythonapp || true
docker rm mypythonapp || true
