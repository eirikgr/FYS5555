!******************************************************************
module store_pathname
!******************************************************************
 implicit none

 integer,parameter:: pathname_length= 96
 character(len=pathname_length),parameter :: pathname= &
     &     "/home/eirikgr/Documents/SUSYPheno/DARKSUSY/darksusy-5.1.1/contrib/HiggsBounds-3.8.1/HiggsBounds" // &
     &     "/"

end module store_pathname
!******************************************************************
