Name:           ros-kinetic-realsense-camera
Version:        1.5.0
Release:        0%{?dist}
Summary:        ROS realsense_camera package

Group:          Development/Libraries
License:        BSD 3-clause. See license attached
URL:            http://www.ros.org/wiki/RealSense
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-camera-info-manager
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-librealsense
Requires:       ros-kinetic-message-generation
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-pcl-ros
Requires:       ros-kinetic-rgbd-launch
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rostest
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-camera-info-manager
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-librealsense >= 0.9.2
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-pcl-ros
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf

%description
RealSense Camera package allowing access to Intel 3D cameras and advanced
modules

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Sep 29 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.5.0-0
- Autogenerated by Bloom

* Thu Aug 25 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.4.0-0
- Autogenerated by Bloom

* Thu Jul 28 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.3.0-0
- Autogenerated by Bloom

* Wed Jul 13 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.1-0
- Autogenerated by Bloom

* Thu Jun 30 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.2.0-0
- Autogenerated by Bloom

* Mon Jun 20 2016 Rajvi Jingar <rajvi.jingar@intel.com> - 1.1.0-0
- Autogenerated by Bloom

