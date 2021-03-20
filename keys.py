import enum

__all__ = ["KeyBinds"]


class KeyBinds(enum.Enum):
    """https://docs.unrealengine.com/udk/Three/KeyBinds.html#Mappable%20keys"""

    # make variants return their value, not their name
    def __str__(self) -> str:
        return str(self.value)

    #
    # Function keys
    #

    # Function one.
    F1 = "F1"
    # Function two.
    F2 = "F2"
    # Function three.
    F3 = "F3"
    # Function four.
    F4 = "F4"
    # Function five.
    F5 = "F5"
    # Function six.
    F6 = "F6"
    # Function seven.
    F7 = "F7"
    # Function eight.
    F8 = "F8"
    # Function nine.
    F9 = "F9"
    # Function ten.
    F10 = "F10"
    # Function eleven.
    F11 = "F11"
    # Function twelve.
    F12 = "F12"

    #
    # Alphanumerical keys
    #

    # Letter A.
    A = "A"
    # Letter B.
    B = "B"
    # Letter C.
    C = "C"
    # Letter D.
    D = "D"
    # Letter E.
    E = "E"
    # Letter F.
    F = "F"
    # Letter G.
    G = "G"
    # Letter H.
    H = "H"
    # Letter I.
    I = "I"  # noqa: E741
    # Letter J.
    J = "J"
    # Letter K.
    K = "K"
    # Letter L.
    L = "L"
    # Letter M.
    M = "M"
    # Letter N.
    N = "N"
    # Letter O.
    O = "O"  # noqa: E741
    # Letter P.
    P = "P"
    # Letter Q.
    Q = "Q"
    # Letter R.
    R = "R"
    # Letter S.
    S = "S"
    # Letter T.
    T = "T"
    # Letter U.
    U = "U"
    # Letter V.
    V = "V"
    # Letter W.
    W = "W"
    # Letter X.
    X = "X"
    # Letter Y.
    Y = "Y"
    # Letter Z.
    Z = "Z"

    #
    # Special keys
    #

    # Escape.
    Escape = "Escape"
    # Tab.
    Tab = "Tab"
    # ~.
    Tilde = "Tilde"
    # Scroll lock.
    ScrollLock = "ScrollLock"
    # Pause.
    Pause = "Pause"
    # One.
    One = "one"
    # Two.
    Two = "two"
    # Three.
    Three = "three"
    # Four.
    Four = "four"
    # Five.
    Five = "five"
    # Six.
    Six = "six"
    # Seven.
    Seven = "seven"
    # Eight.
    Eight = "eight"
    # Nine.
    Nine = "nine"
    # Zero.
    Zero = "zero"
    # _.
    Underscore = "Underscore"
    # =.
    Equals = "Equals"
    # \.
    Backslash = "Backslash"
    # [.
    LeftBracket = "LeftBracket"
    # ].
    RightBracket = "RightBracket"
    # Enter or Numpad enter.
    Enter = "Enter"
    # Caps lock.
    CapsLock = "CapsLock"
    # ;.
    Semicolon = "Semicolon"
    # '.
    Quote = "Quote"
    # Left shift.
    LeftShift = "LeftShift"
    # ,.
    Comma = "Comma"
    # ..
    Period = "Period"
    # /.
    Slash = "Slash"
    # Right Shift
    RightShift = "RightShift"
    # Left control.
    LeftControl = "LeftControl"
    # Left alt.
    LeftAlt = "LeftAlt"
    # Space bar.
    SpaceBar = "SpaceBar"
    # Right alt.
    RightAlt = "RightAlt"
    # Right control.
    RightControl = "RightControl"
    # Left.
    Left = "Left"
    # Up.
    Up = "Up"
    # Down.
    Down = "Down"
    # Right.
    Right = "Right"
    # Home.
    Home = "Home"
    # End.
    End = "End"
    # Insert.
    Insert = "Insert"
    # Page up.
    PageUp = "PageUp"
    # Delete.
    Delete = "Delete"
    # Page down.
    PageDown = "PageDown"
    # Num lock.
    NumLock = "NumLock"
    # Numpad /.
    Divide = "Divide"
    # Numpad *.
    Multiply = "Multiply"
    # Numpad -.
    Subtract = "Subtract"
    # Numpad +.
    Add = "Add"
    # Numpad one.
    NumPadOne = "NumPadOne"
    # Numpad two.
    NumPadTwo = "NumPadTwo"
    # Numpad three.
    NumPadThree = "NumPadThree"
    # Numpad four.
    NumPadFour = "NumPadFour"
    # Numpad five.
    NumPadFive = "NumPadFive"
    # Numpad six.
    NumPadSix = "NumPadSix"
    # Numpad seven.
    NumPadSeven = "NumPadSeven"
    # Numpad eight.
    NumPadEight = "NumPadEight"
    # Numpad nine.
    NumPadNine = "NumPadNine"
    # Numpad zero.
    NumPadZero = "NumPadZero"
    # Numpad decimal.
    NumPadDecimal = "Decimal"

    #
    # Mouse
    #

    # Left mouse button.
    LeftMouseButton = "LeftMouseButton"
    # Right mouse button.
    RightMouseButton = "RightMouseButton"
    # Primary mouse thumb button.
    ThumbMouseButton = "ThumbMouseButton"
    # Secondary mouse thumb button.
    ThumbMouseButton2 = "ThumbMouseButton2"
    # Mouse wheel scrolling up.
    MouseScrollUp = "MouseScrollUp"
    # Mouse wheel scrolling down.
    MouseScrollDown = "MouseScrollDown"
    # Mouse movement on the X axis.
    MouseX = "MouseX"
    # Mouse movement on the Y axis.
    MouseY = "MouseY"

    #
    # XBox360 Controller
    #

    # Left thumb stick when pressed as a button.
    GamePad_LeftThumbStick = "XboxTypeS_LeftThumbStick"
    # Right thumb stick when pressed as a button.
    GamePad_RightThumbStick = "XboxTypeS_RightThumbStick"
    # Directional pad up.
    GamePad_DPad_Up = "XboxTypeS_DPad_Up"
    # Directional pad left.
    GamePad_DPad_Left = "XboxTypeS_DPad_Left"
    # Directional pad right.
    GamePad_DPad_Right = "XboxTypeS_DPad_Right"
    # Directional pad down.
    GamePad_DPad_Down = "XboxTypeS_DPad_Down"
    # Back button.
    GamePad_Back = "XboxTypeS_Back"
    # Start button.
    GamePad_Start = "XboxTypeS_Start"
    # Y button.
    GamePad_Y = "XboxTypeS_Y"
    # X button.
    GamePad_X = "XboxTypeS_X"
    # B button.
    GamePad_B = "XboxTypeS_B"
    # A button.
    GamePad_A = "XboxTypeS_A"
    # Left shoulder button.
    GamePad_LeftShoulder = "XboxTypeS_LeftShoulder"
    # Right shoulder button.
    GamePad_RightShoulder = "XboxTypeS_RightShoulder"
    # Left trigger when pressed as a button.
    GamePad_LeftTrigger = "XboxTypeS_LeftTrigger"
    # Right trigger when pressed as a button.
    GamePad_RightTrigger = "XboxTypeS_RightTrigger"
    # Left trigger when semi depressed.
    GamePad_LeftTriggerAxis = "XboxTypeS_LeftTriggerAxis"
    # Right trigger when semi depressed.
    GamePad_RightTriggerAxis = "XboxTypeS_RightTriggerAxis"
    # Left thumb stick horizontal position when used as an analogue control.
    GamePad_LeftX = "XboxTypeS_LeftX"
    # Left thumb stick vertical position when used as an analogue control.
    GamePad_LeftY = "XboxTypeS_LeftY"
    # Right thumb stick horizontal position when used as an analogue control.
    GamePad_RightX = "XboxTypeS_RightX"
    # Right thumb stick vertical position when used as an analogue control.
    GamePad_RightY = "XboxTypeS_RightY"
