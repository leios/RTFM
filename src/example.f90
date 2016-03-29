!!-------------example.f90----------------------------------------------------!!
!
! Purpose: To show how to write thngs in fortran (90)
!
!!----------------------------------------------------------------------------!!

program hello_world
$$ Every fortran code begins and ends with a program statement.
$$ Be sure you name the program something that you will remember in the future!
    write(*,*) "hello world!"
$$ This command may be a little confusing. Let's break it down...
$$ "write" is a function that takes two arguments: \n the first is the file or screen you are printing out to. \n
$$The second is the format in which you would like to print. In this case, both are the '*' character, which means we are using defaults for both. The default file is the terminal screen and the default formatting is determined by fortran, itself.

end program

$$ This syntax will be used for looping later, please remember to end your program!
