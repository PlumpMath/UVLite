#pragma once

#ifdef __cplusplus
extern "C" {
#endif

#include <stdio.h>
#include <stdbool.h>

#ifdef _WIN32
    // Windows - set up dll import/export decorators.
    #ifdef BUILDING_UVLITE_SHARED
        // Building shared library.
        #define UVLITE_EXTERN __declspec(dllexport)
    #else
        #ifdef USING_UVLITE_SHARED
            // Using shared library.
            #define UVLITE_EXTERN __declspec(dllimport)
        #else
            // Building static library.
            #define UVLITE_EXTERN // nothing 
        #endif
    #endif

    #define UVLITE_CALLING_CONVENTION __cdecl
#else
    // Building static library.
    #define UVLITE_EXTERN // nothing 
    #define UVLITE_CALLING_CONVENTION // nothing 
#endif

UVLITE_EXTERN int foo1();
UVLITE_EXTERN int foo2();

#ifdef __cplusplus
}
#endif
