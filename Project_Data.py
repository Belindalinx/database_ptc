﻿'''#######################################################
    This module contains the Project Data lists
      - Product: l_prod
          Index 0 = Product number - String
          Index 1 = Product line   - String
          Index 2 = Size           - String
          Index 3 = Color          - String
          Index 4 = Price          - Float
      - Order:   l_order
          Index 0 = Order number   - Integer
          Index 1 = Product number - String
          Index 2 = Order quantity - Integer
          Index 3 = Order date     - String
      
##########################################################'''
## ======================
## Products
## ======================
l_prod = [
  ['tray-lw', 'tray', 'Large', 'White', 12.25],
  ['tray-lg', 'tray', 'Large', 'Green', 12.75],
  ['tray-mw', 'tray', 'Medium', 'White', 11.5],
  ['tray-mg', 'tray', 'Medium', 'Green', 11.5],
  ['vial-lw', 'vial holder', 'Large', 'White', 9.0],
  ['vial-lg', 'vial holder', 'Large', 'Green', 9.0],
  ['vial-mw', 'vial holder', 'Medium', 'White', 7.5],
  ['vial-mg', 'vial holder', 'Medium', 'Green', 7.5],
  ['vial-sw', 'vial holder', 'Small', 'White', 15.5],
  ['vial-sg', 'vial holder', 'Small', 'Green', 15.5],
  ['sample-c', 'sample container', 'Medium', 'Clear', 14.25],
  ['sample-g', 'sample container', 'Medium', 'White', 11.50],
];




## ======================
## Orders
## ======================
l_ord = [
  [4115, 'tray-mw',  11, '2017-07-29' ] ,
  [4116, 'tray-mw',  19, '2017-09-11' ] ,
  [4117, 'vial-lw',  17, '2017-09-19' ] ,
  [4118, 'vial-mw',  19, '2017-08-09' ] ,
  [4119, 'vial-sw',  17, '2017-07-18' ] ,
  [4120, 'vial-mg',  24, '2017-08-29' ] ,
  [4121, 'vial-mg',  25, '2017-08-03' ] ,
  [4122, 'vial-sg',  11, '2017-09-26' ] ,
  [4123, 'sample-g',  23, '2017-09-17' ] ,
  [4124, 'vial-lw',  8, '2017-07-27' ] ,
  [4125, 'vial-sg',  13, '2017-07-10' ] ,
  [4126, 'vial-sw',  21, '2017-08-19' ] ,
  [4127, 'sample-g',  17, '2017-09-01' ] ,
  [4128, 'vial-lw',  22, '2017-09-16' ] ,
  [4129, 'vial-mg',  22, '2017-07-28' ] ,
  [4130, 'vial-mg',  16, '2017-07-15' ] ,
  [4131, 'vial-sw',  17, '2017-09-16' ] ,
  [4132, 'vial-lw',  24, '2017-07-29' ] ,
  [4133, 'tray-mw',  29, '2017-08-22' ] ,
  [4134, 'vial-lw',  30, '2017-08-30' ] ,
  [4135, 'sample-g',  17, '2017-09-02' ] ,
  [4136, 'vial-lw',  26, '2017-08-11' ] ,
  [4137, 'vial-sw',  27, '2017-07-30' ] ,
  [4138, 'tray-lg',  22, '2017-09-22' ] ,
  [4139, 'tray-mw',  23, '2017-09-17' ] ,
  [4140, 'vial-mg',  20, '2017-09-03' ] ,
  [4141, 'vial-sw',  5, '2017-09-03' ] ,
  [4142, 'sample-g',  5, '2017-07-21' ] ,
  [4143, 'tray-lg',  11, '2017-07-28' ] ,
  [4144, 'vial-lw',  6, '2017-07-28' ] ,
  [4145, 'vial-mw',  10, '2017-09-25' ] ,
  [4146, 'vial-mw',  29, '2017-07-12' ] ,
  [4147, 'vial-sg',  19, '2017-07-19' ] ,
  [4148, 'vial-mw',  16, '2017-09-07' ] ,
  [4149, 'sample-g',  8, '2017-08-17' ] ,
  [4150, 'sample-g',  20, '2017-09-12' ] ,
  [4151, 'tray-lg',  6, '2017-09-20' ] ,
  [4152, 'tray-lg',  26, '2017-08-02' ] ,
  [4153, 'vial-mw',  11, '2017-07-05' ] ,
  [4154, 'vial-mw',  5, '2017-08-22' ] ,
  [4155, 'vial-sw',  6, '2017-08-24' ] ,
  [4156, 'vial-sw',  10, '2017-07-17' ] ,
  [4157, 'tray-mg',  14, '2017-08-26' ] ,
  [4158, 'vial-sg',  7, '2017-08-17' ] ,
  [4159, 'sample-g',  22, '2017-08-11' ] ,
  [4160, 'vial-mg',  18, '2017-09-09' ] ,
  [4161, 'tray-lg',  27, '2017-08-02' ] ,
  [4162, 'tray-mg',  8, '2017-09-09' ] ,
  [4163, 'tray-mw',  22, '2017-07-10' ] ,
  [4164, 'vial-mw',  13, '2017-08-29' ] ,
  [4165, 'vial-sg',  5, '2017-07-14' ] ,
  [4166, 'vial-sw',  25, '2017-07-03' ] ,
  [4167, 'tray-lg',  10, '2017-09-08' ] ,
  [4168, 'tray-mw',  11, '2017-09-27' ] ,
  [4169, 'vial-lw',  7, '2017-07-06' ] ,
  [4170, 'vial-mg',  17, '2017-09-12' ] ,
  [4171, 'vial-sg',  20, '2017-07-06' ] ,
  [4172, 'tray-mg',  16, '2017-09-22' ] ,
  [4173, 'tray-mg',  10, '2017-07-11' ] ,
  [4174, 'tray-mg',  23, '2017-07-16' ] ,
  [4175, 'tray-mg',  24, '2017-09-06' ] ,
  [4176, 'tray-mw',  25, '2017-08-16' ] ,
  [4177, 'vial-mw',  9, '2017-09-16' ] ,
  [4178, 'vial-sg',  9, '2017-09-04' ] ,
  [4179, 'sample-g',  19, '2017-09-29' ] ,
  [4180, 'tray-mg',  13, '2017-09-07' ] ,
  [4181, 'vial-mg',  20, '2017-08-07' ] ,
  [4182, 'vial-sw',  24, '2017-07-16' ] ,
  [4183, 'tray-mw',  13, '2017-08-04' ] ,
  [4184, 'vial-lw',  24, '2017-09-16' ] ,
  [4185, 'vial-sg',  25, '2017-08-03' ] ,
  [4186, 'tray-mw',  16, '2017-09-26' ] ,
  [4187, 'vial-mw',  13, '2017-07-17' ] ,
  [4188, 'vial-sg',  28, '2017-07-02' ] ,
  [4189, 'sample-g',  8, '2017-08-06' ] ,
  [4190, 'tray-lg',  24, '2017-08-27' ] ,
  [4191, 'tray-mg',  30, '2017-09-22' ] ,
  [4192, 'vial-lw',  10, '2017-07-09' ] ,
  [4193, 'tray-lg',  22, '2017-07-11' ] ,
  [4194, 'tray-lg',  29, '2017-08-09' ] ,
  [4195, 'tray-mg',  18, '2017-07-02' ] ,
  [4196, 'vial-mg',  8, '2017-09-10' ] ,
  [4197, 'vial-mg',  15, '2017-08-13' ] ,
  [4198, 'vial-mw',  7, '2017-08-26' ] ,
  [4199, 'vial-sg',  21, '2017-07-29' ] ,
  [4200, 'vial-sw',  24, '2017-09-10' ] ,
  [4201, 'tray-lg',  28, '2017-09-01' ] ,
  [4202, 'tray-lg',  21, '2017-07-12' ] ,
  [4203, 'tray-mw',  9, '2017-08-13' ] ,
  [4204, 'vial-mg',  25, '2017-07-03' ] ,
  [4205, 'vial-lw',  26, '2017-08-13' ] ,
  [4206, 'vial-mg',  20, '2017-08-18' ] ,
  [4207, 'vial-mw',  14, '2017-07-23' ] ,
  [4208, 'vial-sg',  29, '2017-07-12' ] ,
  [4209, 'sample-g',  8, '2017-07-22' ] ,
  [4210, 'tray-mg',  6, '2017-07-12' ] ,
  [4211, 'tray-mg',  12, '2017-07-27' ] ,
  [4212, 'sample-g',  18, '2017-07-14' ] ,
  [4213, 'tray-mw',  10, '2017-09-11' ] ,
  [4214, 'vial-sw',  27, '2017-07-17' ] ,
 ]