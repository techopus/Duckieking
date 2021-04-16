FROM duckietown/dt-gui-tools:daffy-amd64
COPY /source /source
ENV VEHICLE_NAME=duckiequeen
ENV ROS_MASTER=duckiequeen
ENV DUCKIEBOT_NAME=duckiequeen
ENV ROS_MASTER_URI=http://duckiequeen.local:11311
ENV HOSTNAME=duckiequeen
CMD ["chmod +x /source/main.py"]
CMD ["/source/main.py"]