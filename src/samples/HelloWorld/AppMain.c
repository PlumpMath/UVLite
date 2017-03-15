#include <stdio.h>
#include <stdlib.h>
#include <uv.h>

#include "UVLite.h"
#include "Sample1.h"

int main(int args, char** argsv)
{
    // lets compile a simple libuv program. 
    // It has no events to process so it does nothing, 
    // except start a loop which will exit immediately.
    // because a libuv event loop has to be told to watch out for events

    uv_loop_t *loop = malloc(sizeof(uv_loop_t));
    uv_loop_init(loop);

    printf("Now quitting.\n");
    uv_run(loop, UV_RUN_DEFAULT);

    uv_loop_close(loop);
    free(loop);

    return 0;
}

