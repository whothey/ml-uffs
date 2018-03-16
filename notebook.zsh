#! /bin/zsh

if [[ $# == 0 ]] || [[ $1 = 'run' ]]; then
    FLAGS=-d
elif [[ $1 = 'interactive' ]] || [[ $1 = 'it' ]]; then
    FLAGS=-it
fi;

docker run $FLAGS --rm -p 8888:8888 -v $PWD:/home/jovyan/work jupyter/scipy-notebook
