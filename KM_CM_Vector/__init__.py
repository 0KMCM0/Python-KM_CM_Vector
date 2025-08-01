"""
https://github.com/0KMCM0/Python-KM_CM_Vector
"""

from typing import Generic as _Generic, TypeVar as _TypeVar

_T = _TypeVar( '_T' )

class Vector( _Generic[ _T ] ):
    """
A mathematical ``Vector`` that goes on way beyond math, allowing to use it with any type.
    """

    def __init__( self, *Axes: _T ) -> None:
        """
Initializes the ``Vector``.
        """
        self.m_lAxes: list[ _T ] = list( Axes )

    def Magnitude( self ) -> _T:
        """
Returns the magnitude of the ``Vector``, which is
the square root of the sum of all elements squared.
        """
        return sum( X ** 2 for X in self.m_lAxes ) ** .5
    def Distance( self, Other: 'Vector[ _T ]' ) -> _T:
        """
Returns the Eucledian distance between the ``Vector``'s.
        """
        return sum( ( A - B ) ** 2 for A, B in zip( self.m_lAxes, Other.m_lAxes ) ) ** .5

    def Dot( self, Other: 'Vector[ _T ]' ) -> _T:
        """
Returns the dot product of 2 ``Vector``'s.
|A||B|cos
        """
        return sum( A * B for A, B in zip( self.m_lAxes, Other.m_lAxes ) )

    def __str__( self ) -> str:
        """
Returns the string representation of the ``Vector``.
        """
        return self.m_lAxes and f'Vector[ { ', '.join( [ repr( X ) for X in self.m_lAxes ] ) } ]' or 'Vector[]'
    def __repr__( self ) -> str:
        """
Returns the code representation of the ``Vector``.
        """
        return self.m_lAxes and f'Vector({ ','.join( [ repr( X ) for X in self.m_lAxes ] ) })' or 'Vector()'

    def __abs__( self ) -> 'Vector[ _T ]':
        """
Returns the absolute of the ``Vector``.
        """
        return Vector( *( abs( X ) for X in self.m_lAxes ) )
    def __neg__( self ) -> 'Vector[ _T ]':
        """
Returns the opposite of the ``Vector``.
        """
        return Vector( *( -X for X in self.m_lAxes ) )

    def __setitem__( self, Index: int, Value: _T ) -> None:
        """
Set axis ``Index + 1`` to ``Value``.
        """
        self.m_lAxes[ Index ] = Value
    def __getitem__( self, Index: int ) -> _T:
        """
Get axis ``Index + 1``.
        """
        return self.m_lAxes[ Index ]

    def __Operator__( self, Other, Func ) -> 'Vector[ _T ]':
        if isinstance( Other, Vector ):
            return Vector( *( Func( X, Y ) for X, Y in zip( self.m_lAxes, Other.m_lAxes ) ) )
        return Vector( *( Func( X, Other ) for X in self.m_lAxes ) )

    def __ROperator__( self, Other, Func ) -> 'Vector[ _T ]':
        if isinstance( Other, Vector ):
            return Vector( *( Func( Y, X ) for X, Y in zip( self.m_lAxes, Other.m_lAxes ) ) )
        return Vector( *( Func( Other, X ) for X in self.m_lAxes ) )

    def __add__( self, Other ) -> 'Vector[ _T ]': return      self.__Operator__( Other, lambda A, B: A + B )
    def __sub__( self, Other ) -> 'Vector[ _T ]': return      self.__Operator__( Other, lambda A, B: A - B )
    def __mul__( self, Other ) -> 'Vector[ _T ]': return      self.__Operator__( Other, lambda A, B: A * B )
    def __pow__( self, Other ) -> 'Vector[ _T ]': return      self.__Operator__( Other, lambda A, B: A ** B )
    def __mod__( self, Other ) -> 'Vector[ _T ]': return      self.__Operator__( Other, lambda A, B: A % B )
    def __truediv__( self, Other ) -> 'Vector[ _T ]': return  self.__Operator__( Other, lambda A, B: A / B )
    def __floordiv__( self, Other ) -> 'Vector[ _T ]': return self.__Operator__( Other, lambda A, B: A // B )

    def __radd__( self, Other ) -> 'Vector[ _T ]': return      self.__ROperator__( Other, lambda A, B: A + B )
    def __rsub__( self, Other ) -> 'Vector[ _T ]': return      self.__ROperator__( Other, lambda A, B: A - B )
    def __rmul__( self, Other ) -> 'Vector[ _T ]': return      self.__ROperator__( Other, lambda A, B: A * B )
    def __rpow__( self, Other ) -> 'Vector[ _T ]': return      self.__ROperator__( Other, lambda A, B: A ** B )
    def __rmod__( self, Other ) -> 'Vector[ _T ]': return      self.__ROperator__( Other, lambda A, B: A % B )
    def __rtruediv__( self, Other ) -> 'Vector[ _T ]': return  self.__ROperator__( Other, lambda A, B: A / B )
    def __rfloordiv__( self, Other ) -> 'Vector[ _T ]': return self.__ROperator__( Other, lambda A, B: A // B )
