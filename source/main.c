#include <nds.h>
#include "stdio.h"

int main(void) {

  consoleDemoInit();

  printf("Hello World!\n");

  while(1) {
    swiWaitForVBlank();
  }

  return 0;
}
