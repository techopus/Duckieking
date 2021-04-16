FROM duckietown/dt-gui-tools:daffy-amd64
COPY /source /source
ENV VEHICLE_NAME=localhost
ENV ROS_MASTER=localhost
ENV DUCKIEBOT_NAME=localhost
ENV ROS_MASTER_URI=http://localhost:11311
ENV HOSTNAME=localhost
CMD ["chmod +x /source/main.py"]
CMD ["/source/main.py"]