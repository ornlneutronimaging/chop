import numpy as np

Mn=1.67e-27 #Mass of Neutrons (kg)
h=6.60e-34 #Planck's const (Js)

CF=(h*1e7)/Mn #(3.952) time should be in milisecond and wavelength should be in angstrom

class VENUS_chopper(object):

    def __init__(self, Pulse_frequency, pulse_width,delay ,SourceTOdetector , chopper_rotational_frequency,wavelength_center):
        r"""

        Parameters
        ----------
        Pulse_frequency: float
            Pulse_frequency of neutron source in Hz

        pulse_width: float
            Neutrons emitted from the moderator with a certain wavelength
            :math:`\lambda` have a distribution of delayed emission times
            with :math:`FWHM(\lambda) \simeq pulsewidth \cdot \lambda`.
            Units are seconds/Angstroms.

        delay: float
            Additional time-of-flight to include in the calculations

        SourceTOdetector: float
            Distance travelled by the neutron to detector, in meters

        chopper_rotational_frequency: float
            rotational frequency of chopper, in Hz

        wavelength_center: float
            wavelength  center of the arriving neutron, in Angstrom
        """
        self.Pulse_frequency = Pulse_frequency
        self.pulse_width= float(pulse_width)
        self.delay = float(delay)
        self.SourceTOdetector= float(SourceTOdetector)
        self.chopper_rotational_frequency=chopper_rotational_frequency
        self.wavelength_center=wavelength_center

    def Wavelength(self,frequency,distance):
        r"""
         neutron wavelength for a particular frequency and distance travelled
        ----------
        distance: float
            distance travelled by neutrons, in meters
        frequency: float
            frequncy  in Hz

        Returns
        -------
        float
            wavelength (in Angstrom)
        """
        frequency = frequency / 1000
        time=(1/frequency)+ self.pulse_width

        return CF*(time/distance)


    def tof(self, distance, wavelength, pulsed=False):
        r"""
        Convert wavelength of arriving neutron to time of flight

        Parameters
        ----------
        wavelength: float
            wavelength of the arriving neutron, in Angstrom
        distance: float
            distance travelled by neutrons, in meters
        pulsed: bool
            Include the correction due to delayed emission of neutrons
            from the moderator

        Returns
        -------
        float
            time of flight (in milisecond)
        """

        loc = distance
        if pulsed is True:
            loc += CF * self.pulse_width
        return wavelength * loc / CF - self.delay


    def Chopper_open_duration(self, distance):
        r"""
          calculated the acceptable open duration of chopper

          Parameters
          ----------
          distance: float
              distance travelled by neutrons to chopper, in meters

          Returns
          -------
          float
              Open duration of chopper, in milisecond
          """
        chopper_open_Duration= (self.frame_time_width()/self.SourceTOdetector)*distance
        return(chopper_open_Duration)


    def Chopper_phase_angle(self, distance): #Open Angle
        r"""
          calculated the phase angle

          Parameters
          ----------
          distance: float
              distance travelled by neutrons to chopper, in meters

          Returns
          -------
          float
              Opening window, in degrees
          """
        angular_velocity=self.chopper_rotational_frequency*2*np.pi
        radTodeg=360/(2*np.pi)
        return(self.Chopper_open_duration(distance)*angular_velocity*radTodeg)


    def frame_wavelength_width(self):
        r"""
          calculated frame acceptable wavelength width

          Returns
          -------
          float
              acceptable wavelength width , in Hz
          """
        return (self.Wavelength(self.Pulse_frequency, self.SourceTOdetector))



    def initial_final_wavelength(self, wavelengthType):
        r"""
          calculated acceptable initial and final wavelength from wavelength center

          Parameters
          ----------
          wavelengthType: string
              initial_wavelength, final_wavelength

          Returns
          -------
          float
              Acceptable initial and final wavelength, in Hz
          """
        w={'initial_wavelength' : self.wavelength_center - self.frame_wavelength_width() / 2,
            'final_wavelength' : (self.wavelength_center + self.frame_wavelength_width() / 2)}
        return w[wavelengthType]

    def min_max_tof(self, tofType):
        r"""
          calculated acceptable maximum and minimum time of flight

          Parameters
          ----------
          tofType: string
              max_tof, min_tof

          Returns
          -------
          float
              Acceptable maximum and minimum tof, in milisecond
          """
        tof_max = self.tof(self.SourceTOdetector, self.initial_final_wavelength('final_wavelength'))
        tof_min = self.tof(self.SourceTOdetector, self.initial_final_wavelength('initial_wavelength'))

        t = {'max_tof':tof_max,
             'min_tof':tof_min }
        return t [tofType]


    def frame_time_width(self):
        r"""
        Acceptable Frame time width calculation

        Returns
        -------
        float
            Acceptable frame time width (in miliseconds)
        """
        return (self.min_max_tof('max_tof')-self.min_max_tof('min_tof'))


