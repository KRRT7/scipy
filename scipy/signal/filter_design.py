# This file is not meant for public use and will be removed in SciPy v2.0.0.
# Use the `scipy.signal` namespace for importing the functions
# included below.

from importlib import import_module

from scipy._lib.deprecation import _sub_module_deprecation

__all__ = [  # noqa: F822
    'findfreqs', 'freqs', 'freqz', 'tf2zpk', 'zpk2tf', 'normalize',
    'lp2lp', 'lp2hp', 'lp2bp', 'lp2bs', 'bilinear', 'iirdesign',
    'iirfilter', 'butter', 'cheby1', 'cheby2', 'ellip', 'bessel',
    'band_stop_obj', 'buttord', 'cheb1ord', 'cheb2ord', 'ellipord',
    'buttap', 'cheb1ap', 'cheb2ap', 'ellipap', 'besselap',
    'BadCoefficients', 'freqs_zpk', 'freqz_zpk',
    'tf2sos', 'sos2tf', 'zpk2sos', 'sos2zpk', 'group_delay',
    'sosfreqz', 'freqz_sos', 'iirnotch', 'iirpeak', 'bilinear_zpk',
    'lp2lp_zpk', 'lp2hp_zpk', 'lp2bp_zpk', 'lp2bs_zpk',
    'gammatone', 'iircomb',
]


def __dir__():
    return __all__


def __getattr__(name):
    return _sub_module_deprecation(
        sub_package="signal", module="filter_design",
        private_modules=["_filter_design"], all=__all__,
        attribute=name
    )


def _get_attribute_from_private_modules(sub_package, private_modules, attribute):
    """Helper function to attempt importing an attribute from a list of private modules."""
    for module in private_modules:
        try:
            # Attempt to import the attribute from the current module
            return getattr(import_module(f"scipy.{sub_package}.{module}"), attribute)
        except AttributeError:
            # Continue if the attribute isn't in the current private module
            continue
    # If the loop completes without returning, raise an AttributeError
    raise AttributeError(
        f"Module `scipy.{sub_package}.{module}` has no attribute `{attribute}`."
    )
