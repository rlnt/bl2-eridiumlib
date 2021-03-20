import enum

__all__ = ["KeyBinds"]


class KeyBinds(enum.Enum):
    """https://docs.unrealengine.com/udk/Three/KeyBinds.html#Mappable%20keys"""

    # make variants return their value, not their name
    def __str__(self) -> str:
        return str(self.value)

    # Function keys
    F1 = "F1"  # Function one.
    F2 = "F2"  # Function two.
    F3 = "F3"  # Function three.
    F4 = "F4"  # Function four.
    F5 = "F5"  # Function five.
    F6 = "F6"  # Function six.
    F7 = "F7"  # Function seven.
    F8 = "F8"  # Function eight.
    F9 = "F9"  # Function nine.
    F10 = "F10"  # Function ten.
    F11 = "F11"  # Function eleven.
    F12 = "F12"  # Function twelve.

    # Alphanumerical keys
    A = "A"  # Letter A.
    B = "B"  # Letter B.
    C = "C"  # Letter C.
    D = "D"  # Letter D.
    E = "E"  # Letter E.
    F = "F"  # Letter F.
    G = "G"  # Letter G.
    H = "H"  # Letter H.
    I = "I"  # Letter I. # noqa: E741
    J = "J"  # Letter J.
    K = "K"  # Letter K.
    L = "L"  # Letter L.
    M = "M"  # Letter M.
    N = "N"  # Letter N.
    O = "O"  # Letter O. # noqa: E741
    P = "P"  # Letter P.
    Q = "Q"  # Letter Q.
    R = "R"  # Letter R.
    S = "S"  # Letter S.
    T = "T"  # Letter T.
    U = "U"  # Letter U.
    V = "V"  # Letter V.
    W = "W"  # Letter W.
    X = "X"  # Letter X.
    Y = "Y"  # Letter Y.
    Z = "Z"  # Letter Z.

    # Special keys
    Escape = "Escape"  # Escape.
    Tab = "Tab"  # Tab.
    Tilde = "Tilde"  # ~.
    ScrollLock = "ScrollLock"  # Scroll lock.
    Pause = "Pause"  # Pause.
    One = "one"  # One.
    Two = "two"  # Two.
    Three = "three"  # Three.
    Four = "four"  # Four.
    Five = "five"  # Five.
    Six = "six"  # Six.
    Seven = "seven"  # Seven.
    Eight = "eight"  # Eight.
    Nine = "nine"  # Nine.
    Zero = "zero"  # Zero.
    Underscore = "Underscore"  # _.
    Equals = "Equals"  # =.
    Backslash = "Backslash"  # \.
    LeftBracket = "LeftBracket"  # [.
    RightBracket = "RightBracket"  # ].
    Enter = "Enter"  # Enter or Numpad enter.
    CapsLock = "CapsLock"  # Caps lock.
    Semicolon = "Semicolon"  # ;.
    Quote = "Quote"  # '.
    LeftShift = "LeftShift"  # Left shift.
    Comma = "Comma"  # ,.
    Period = "Period"  # ..
    Slash = "Slash"  # /.
    RightShift = "RightShift"  # Right Shift
    LeftControl = "LeftControl"  # Left control.
    LeftAlt = "LeftAlt"  # Left alt.
    SpaceBar = "SpaceBar"  # Space bar.
    RightAlt = "RightAlt"  # Right alt.
    RightControl = "RightControl"  # Right control.
    Left = "Left"  # Left.
    Up = "Up"  # Up.
    Down = "Down"  # Down.
    Right = "Right"  # Right.
    Home = "Home"  # Home.
    End = "End"  # End.
    Insert = "Insert"  # Insert.
    PageUp = "PageUp"  # Page up.
    Delete = "Delete"  # Delete.
    PageDown = "PageDown"  # Page down.
    NumLock = "NumLock"  # Num lock.
    Divide = "Divide"  # Numpad /.
    Multiply = "Multiply"  # Numpad *.
    Subtract = "Subtract"  # Numpad -.
    Add = "Add"  # Numpad +.
    NumPadOne = "NumPadOne"  # Numpad one.
    NumPadTwo = "NumPadTwo"  # Numpad two.
    NumPadThree = "NumPadThree"  # Numpad three.
    NumPadFour = "NumPadFour"  # Numpad four.
    NumPadFive = "NumPadFive"  # Numpad five.
    NumPadSix = "NumPadSix"  # Numpad six.
    NumPadSeven = "NumPadSeven"  # Numpad seven.
    NumPadEight = "NumPadEight"  # Numpad eight.
    NumPadNine = "NumPadNine"  # Numpad nine.
    NumPadZero = "NumPadZero"  # Numpad zero.
    NumPadDecimal = "Decimal"  # Numpad decimal.

    # Mouse
    LeftMouseButton = "LeftMouseButton"  # Left mouse button.
    RightMouseButton = "RightMouseButton"  # Right mouse button.
    ThumbMouseButton = "ThumbMouseButton"  # Primary mouse thumb button.
    ThumbMouseButton2 = "ThumbMouseButton2"  # Secondary mouse thumb button.
    MouseScrollUp = "MouseScrollUp"  # Mouse wheel scrolling up.
    MouseScrollDown = "MouseScrollDown"  # Mouse wheel scrolling down.
    MouseX = "MouseX"  # Mouse movement on the X axis.
    MouseY = "MouseY"  # Mouse movement on the Y axis.

    # XBox360 Controller
    GamePad_LeftThumbStick = (
        "XboxTypeS_LeftThumbStick"  # Left thumb stick when pressed as a button.
    )
    GamePad_RightThumbStick = (
        "XboxTypeS_RightThumbStick"  # Right thumb stick when pressed as a button.
    )
    GamePad_DPad_Up = "XboxTypeS_DPad_Up"  # Directional pad up.
    GamePad_DPad_Left = "XboxTypeS_DPad_Left"  # Directional pad left.
    GamePad_DPad_Right = "XboxTypeS_DPad_Right"  # Directional pad right.
    GamePad_DPad_Down = "XboxTypeS_DPad_Down"  # Directional pad down.
    GamePad_Back = "XboxTypeS_Back"  # Back button.
    GamePad_Start = "XboxTypeS_Start"  # Start button.
    GamePad_Y = "XboxTypeS_Y"  # Y button.
    GamePad_X = "XboxTypeS_X"  # X button.
    GamePad_B = "XboxTypeS_B"  # B button.
    GamePad_A = "XboxTypeS_A"  # A button.
    GamePad_LeftShoulder = "XboxTypeS_LeftShoulder"  # Left shoulder button.
    GamePad_RightShoulder = "XboxTypeS_RightShoulder"  # Right shoulder button.
    GamePad_LeftTrigger = "XboxTypeS_LeftTrigger"  # Left trigger when pressed as a button.
    GamePad_RightTrigger = "XboxTypeS_RightTrigger"  # Right trigger when pressed as a button.
    GamePad_LeftTriggerAxis = "XboxTypeS_LeftTriggerAxis"  # Left trigger when semi depressed.
    GamePad_RightTriggerAxis = "XboxTypeS_RightTriggerAxis"  # Right trigger when semi depressed.
    GamePad_LeftX = (
        "XboxTypeS_LeftX"  # Left thumb stick horizontal position when used as an analogue control.
    )
    GamePad_LeftY = (
        "XboxTypeS_LeftY"  # Left thumb stick vertical position when used as an analogue control.
    )
    GamePad_RightX = "XboxTypeS_RightX"  # Right thumb stick horizontal position when used as an analogue control.
    GamePad_RightY = (
        "XboxTypeS_RightY"  # Right thumb stick vertical position when used as an analogue control.
    )
