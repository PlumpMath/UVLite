{
    'targets': [
      
      ########################################
      # UVLite static library
      ########################################
      {
        'target_name': 'UVLite',
        'product_name': 'UVLite',
        'type': 'static_library',
        'msvs_guid': '5ECEC9E5-8F23-47B6-93E0-C3B328B3BE65',
        
        'dependencies': [
          './lib/libuv/uv.gyp:libuv',
        ],

        'conditions': [
          ['OS=="linux"', {
            'defines': [
              'PLATFORM_LINUX',
              '_GNU_SOURCE',
            ],
            'cflags': [
              '-std=gnu99',
            ],
          }],
          ['OS=="win"', {
            'defines': [
              'PLATFORM_WINDOWS',
            ],
          }, { # OS != "win",
            'defines': [
              'PLATFORM_POSIX',
            ],
          }]
        ],

        'include_dirs': [
          './include',
          './lib/libuv/include',
        ],

        'sources': [
          'include/UVLite.h',
          'src/UVLite/util/util.h',
          'src/UVLite/util/util.c',
          'src/UVLite/UVLite.c',
        ],

      }, # UVLite static library

      ########################################
      # UVLite shared library
      ########################################
      {
        'target_name': 'UVLite_shared',
        'product_name': 'UVLite',
        'type': 'shared_library',
        'msvs_guid': '5ECEC9E5-8F23-47B6-93E0-C3B328B3BE65',
        
        'dependencies': [
          './lib/libuv/uv.gyp:libuv',
        ],

        'conditions': [
          ['OS=="linux"', {
            'defines': [
              'PLATFORM_LINUX',
              '_GNU_SOURCE',
            ],
            'cflags': [
              '-std=gnu99',
            ],
          }],
          ['OS=="win"', {
            'defines': [
              'PLATFORM_WINDOWS',
              'BUILDING_UVLITE_SHARED',
            ],
          }, { # OS != "win",
            'defines': [
              'PLATFORM_POSIX',
            ],
          }]
        ],

        'include_dirs': [
          './include',
          './lib/libuv/include',
        ],

        'sources': [
          'include/UVLite.h',
          'src/UVLite/util/util.h',
          'src/UVLite/util/util.c',
          'src/UVLite/UVLite.c',
        ],

      }, # UVLite shared library

      ########################################
      # HelloWorld sample
      ########################################
      {
        'target_name': 'HelloWorld',
        'product_name': 'HelloWorld',
        'type': 'executable',
        'msvs_guid': '5ECEC9E5-8F23-47B6-93E0-C3B328B3BE66',

        'dependencies': [
          'UVLite',
        ],
        
        'include_dirs': [
          './include',
          './lib/libuv/include',          
        ],

        'sources': [
          'src/samples/HelloWorld/AppMain.c',
          'src/samples/HelloWorld/Sample1.c'
        ],

        'copies': [
        {
          'destination': '<(PRODUCT_DIR)',
          'files': [
            'src/samples/HelloWorld/MySample.conf',
          ],
        }],

      }, # HelloWorld sample

      ########################################
      # MySample2 sample
      ########################################
      {
        'target_name': 'MySample2',
        'product_name': 'MySample2',
        'type': 'executable',
        'msvs_guid': '5ECEC9E5-8F23-47B6-93E0-C3B328B3BE61',

        'dependencies': [
          'UVLite',
        ],
        
        'include_dirs': [
          './include',
          './lib/libuv/include',          
        ],

        'sources': [
          'src/samples/MySample2/program.c',
        ],

      }, # MySample2 sample


      ########################################
      # TCPServer sample
      ########################################
      {
        'target_name': 'TCPServer',
        'product_name': 'TCPServer',
        'type': 'executable',
        'msvs_guid': '5ECEC9E5-8F23-47B6-93E0-C3B328B3BE61',

        'dependencies': [
          'UVLite',
        ],
        
        'include_dirs': [
          './include',
          './lib/libuv/include',          
        ],

        'sources': [
          'src/samples/TCPServer/MyTCPServer.c',
        ],

      }, # TCPServer sample

      ########################################
      # TCPClient sample
      ########################################
      {
        'target_name': 'TCPClient',
        'product_name': 'TCPClient',
        'type': 'executable',
        'msvs_guid': '5ECEC9E5-8F23-47B6-93E0-C3B328B3BE61',

        'dependencies': [
          'UVLite',
        ],
        
        'include_dirs': [
          './include',
          './lib/libuv/include',          
        ],

        'sources': [
          'src/samples/TCPClient/MyTCPClient.c',
        ],

      }, # TCPClient sample
    ],
  }
