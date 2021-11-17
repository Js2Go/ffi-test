#!/usr/bin/env bash
go build -ldflags "-s -w" -o main.dylib -buildmode=c-shared $PWD/src/main.go
# cp main.dylib $PWD/main.dylib

cargo build --release
