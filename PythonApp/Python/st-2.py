#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-15 19:29:15
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


import streamlit as st
# import cv2

# cap = cv2.VideoCapture(0)

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:

#         #cv2.imshow("vedio", frame)
#         st.image(frame)

#         # vedio write
#         #out.write(frame)
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
# cap.release()
# # out.release()
# #cv2.destroyAllWindows()

button=st.button("input")
st.write(button)