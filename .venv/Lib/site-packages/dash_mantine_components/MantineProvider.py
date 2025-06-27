# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class MantineProvider(Component):
    """A MantineProvider component.
antineProvider

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Your application.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- classNamesPrefix (string; optional):
    A prefix for components static classes (for example
    {selector}-Text-root), `mantine` by default.

- colorSchemeManager (dict; optional):
    Used to retrieve/set color scheme value in external storage, by
    default uses `window.localStorage`.

    `colorSchemeManager` is a dict with keys:

    - get (required):
        Function to retrieve color scheme value from external storage,
        for example window.localStorage.

    - set (required):
        Function to set color scheme value in external storage, for
        example window.localStorage.

    - subscribe (required):
        Function to subscribe to color scheme changes triggered by
        external events.

    - unsubscribe (required):
        Function to unsubscribe from color scheme changes triggered by
        external events.

    - clear (required):
        Function to clear value from external storage.

- cssVariablesResolver (dict; optional):
    Function to generate CSS variables based on theme object.

    `cssVariablesResolver` is a dict with keys:


- cssVariablesSelector (string; optional):
    CSS selector to which CSS variables should be added, `:root` by
    default.

- deduplicateCssVariables (boolean; optional):
    Determines whether CSS variables should be deduplicated: if CSS
    variable has the same value as in default theme, it is not added
    in the runtime. `True` by default.

- defaultColorScheme (a value equal to: 'auto', 'dark', 'light'; optional):
    Default color scheme value used when `colorSchemeManager` cannot
    retrieve value from external storage, `light` by default.

- env (a value equal to: 'default', 'test'; optional):
    Environment at which the provider is used, `'test'` environment
    disables all transitions and portals.

- forceColorScheme (a value equal to: 'dark', 'light'; optional):
    Forces color scheme value, if set, MantineProvider ignores
    `colorSchemeManager` and `defaultColorScheme`.

- stylesTransform (dict; optional):
    An object to transform `styles` and `sx` props into css classes,
    can be used with CSS-in-JS libraries.

    `stylesTransform` is a dict with keys:

    - sx (optional)

    - styles (optional)

- theme (dict; optional):
    Theme override object.

    `theme` is a dict with keys:

    - focusRing (a value equal to: 'auto', 'always', 'never'; optional):
        Controls focus ring styles. Supports the following options: -
        `auto` – focus ring is displayed only when the user navigates
        with keyboard (default value) - `always` – focus ring is
        displayed when the user navigates with keyboard and mouse -
        `never` – focus ring is always hidden (not recommended).

    - scale (number; optional):
        Rem units scale, change if you customize font-size of `<html
        />` element default value is `1` (for `100%`/`16px` font-size
        on `<html />`).

    - fontSmoothing (boolean; optional):
        Determines whether `font-smoothing` property should be set on
        the body, `True` by default.

    - white (string; optional):
        White color.

    - black (string; optional):
        Black color.

    - colors (dict; optional):
        Object of colors, key is color name, value is an array of at
        least 10 strings (colors).

        `colors` is a dict with keys:

        - dark (dict with strings as keys and values of type string; optional)

        - gray (dict with strings as keys and values of type string; optional)

        - red (dict with strings as keys and values of type string; optional)

        - pink (dict with strings as keys and values of type string; optional)

        - grape (dict with strings as keys and values of type string; optional)

        - violet (dict with strings as keys and values of type string; optional)

        - indigo (dict with strings as keys and values of type string; optional)

        - blue (dict with strings as keys and values of type string; optional)

        - cyan (dict with strings as keys and values of type string; optional)

        - green (dict with strings as keys and values of type string; optional)

        - lime (dict with strings as keys and values of type string; optional)

        - yellow (dict with strings as keys and values of type string; optional)

        - orange (dict with strings as keys and values of type string; optional)

        - teal (dict with strings as keys and values of type string; optional)

    - primaryShade (optional):
        Index of theme.colors[color]. Primary shade is used in all
        components to determine which color from theme.colors[color]
        should be used. Can be either a number (0–9) or an object to
        specify different color shades for light and dark color
        schemes. Default value `{ light: 6, dark: 8 }`  For example, {
        primaryShade: 6 } // shade 6 is used both for dark and light
        color schemes { primaryShade: { light: 6, dark: 7 } } //
        different shades for dark and light color schemes.

    - primaryColor (string; optional):
        Key of `theme.colors`, hex/rgb/hsl values are not supported.
        Determines which color will be used in all components by
        default. Default value – `blue`.

    - variantColorResolver (dict; optional):
        Function to resolve colors based on variant. Can be used to
        deeply customize how colors are applied to `Button`,
        `ActionIcon`, `ThemeIcon` and other components that use colors
        from theme.

        `variantColorResolver` is a dict with keys:


    - autoContrast (boolean; optional):
        Determines whether text color must be changed based on the
        given `color` prop in filled variant For example, if you pass
        `color=\"blue.1\"` to Button component, text color will be
        changed to `var(--mantine-color-black)` Default value –
        `False`.

    - luminanceThreshold (number; optional):
        Determines which luminance value is used to determine if text
        color should be light or dark. Used only if
        `theme.autoContrast` is set to `True`. Default value is `0.3`.

    - fontFamily (string; optional):
        Font-family used in all components, system fonts by default.

    - fontFamilyMonospace (string; optional):
        Monospace font-family, used in code and other similar
        components, system fonts by default.

    - headings (dict; optional):
        Controls various styles of h1-h6 elements, used in
        TypographyStylesProvider and Title components.

        `headings` is a dict with keys:

        - fontFamily (string; optional)

        - fontWeight (string; optional)

        - textWrap (a value equal to: 'wrap', 'nowrap', 'balance', 'pretty', 'stable'; optional)

        - sizes (dict; optional)

            `sizes` is a dict with keys:

            - h1 (dict; optional)

                `h1` is a dict with keys:

                - fontSize (string; optional)

                - fontWeight (string; optional)

                - lineHeight (string; optional)

            - h2 (dict; optional)

                `h2` is a dict with keys:

                - fontSize (string; optional)

                - fontWeight (string; optional)

                - lineHeight (string; optional)

            - h3 (dict; optional)

                `h3` is a dict with keys:

                - fontSize (string; optional)

                - fontWeight (string; optional)

                - lineHeight (string; optional)

            - h4 (dict; optional)

                `h4` is a dict with keys:

                - fontSize (string; optional)

                - fontWeight (string; optional)

                - lineHeight (string; optional)

            - h5 (dict; optional)

                `h5` is a dict with keys:

                - fontSize (string; optional)

                - fontWeight (string; optional)

                - lineHeight (string; optional)

            - h6 (dict; optional)

                `h6` is a dict with keys:

                - fontSize (string; optional)

                - fontWeight (string; optional)

                - lineHeight (string; optional)

    - radius (dict; optional):
        Object of values that are used to set `border-radius` in all
        components that support it.

        `radius` is a dict with keys:

        - xs (string; optional)

        - sm (string; optional)

        - md (string; optional)

        - lg (string; optional)

        - xl (string; optional)

    - defaultRadius (number; optional):
        Key of `theme.radius` or any valid CSS value. Default
        `border-radius` used by most components.

    - spacing (dict; optional):
        Object of values that are used to set various CSS properties
        that control spacing between elements.

        `spacing` is a dict with keys:

        - xs (string; optional)

        - sm (string; optional)

        - md (string; optional)

        - lg (string; optional)

        - xl (string; optional)

    - fontSizes (dict; optional):
        Object of values that are used to control `font-size` property
        in all components.

        `fontSizes` is a dict with keys:

        - xs (string; optional)

        - sm (string; optional)

        - md (string; optional)

        - lg (string; optional)

        - xl (string; optional)

    - lineHeights (dict; optional):
        Object of values that are used to control `line-height`
        property in `Text` component.

        `lineHeights` is a dict with keys:

        - xs (string; optional)

        - sm (string; optional)

        - md (string; optional)

        - lg (string; optional)

        - xl (string; optional)

    - breakpoints (dict; optional):
        Object of values that are used to control breakpoints in all
        components, values are expected to be defined in em.

        `breakpoints` is a dict with keys:

        - xs (string; optional)

        - sm (string; optional)

        - md (string; optional)

        - lg (string; optional)

        - xl (string; optional)

    - shadows (dict; optional):
        Object of values that are used to add `box-shadow` styles to
        components that support `shadow` prop.

        `shadows` is a dict with keys:

        - xs (string; optional)

        - sm (string; optional)

        - md (string; optional)

        - lg (string; optional)

        - xl (string; optional)

    - respectReducedMotion (boolean; optional):
        Determines whether user OS settings to reduce motion should be
        respected, `False` by default.

    - cursorType (a value equal to: 'default', 'pointer'; optional):
        Determines which cursor type will be used for interactive
        elements - `default` – cursor that is used by native HTML
        elements, for example, `input[type=\"checkbox\"]` has `cursor:
        default` styles - `pointer` – sets `cursor: pointer` on
        interactive elements that do not have these styles by default.

    - defaultGradient (dict; optional):
        Default gradient configuration for components that support
        `variant=\"gradient\"`.

        `defaultGradient` is a dict with keys:

        - from (string; optional)

        - to (string; optional)

        - deg (number; optional)

    - activeClassName (string; optional):
        Class added to the elements that have active styles, for
        example, `Button` and `ActionIcon`.

    - focusClassName (string; optional):
        Class added to the elements that have focus styles, for
        example, `Button` or `ActionIcon`. Overrides `theme.focusRing`
        property.

    - components (dict; optional):
        Allows adding `classNames`, `styles` and `defaultProps` to any
        component.

        `components` is a dict with keys:


    - other (dict; optional):
        Any other properties that you want to access with the theme
        objects.

        `other` is a dict with keys:


- withCssVariables (boolean; optional):
    Determines whether theme CSS variables should be added to given
    `cssVariablesSelector`, `True` by default.

- withGlobalClasses (boolean; optional):
    Determines whether global classes should be added with `<style />`
    tag. Global classes are required for `hiddenFrom`/`visibleFrom`
    and `lightHidden`/`darkHidden` props to work. `True` by default.

- withStaticClasses (boolean; optional):
    Determines whether components should have static classes, for
    example, `mantine-Button-root`. `True` by default."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'MantineProvider'
    ThemeColors = TypedDict(
        "ThemeColors",
            {
            "dark": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "gray": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "red": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "pink": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "grape": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "violet": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "indigo": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "blue": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "cyan": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "green": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "lime": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "yellow": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "orange": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "teal": NotRequired[typing.Dict[typing.Union[str, float, int], str]]
        }
    )

    ThemeVariantColorResolver = TypedDict(
        "ThemeVariantColorResolver",
            {

        }
    )

    ThemeHeadingsSizesH1 = TypedDict(
        "ThemeHeadingsSizesH1",
            {
            "fontSize": NotRequired[str],
            "fontWeight": NotRequired[str],
            "lineHeight": NotRequired[str]
        }
    )

    ThemeHeadingsSizesH2 = TypedDict(
        "ThemeHeadingsSizesH2",
            {
            "fontSize": NotRequired[str],
            "fontWeight": NotRequired[str],
            "lineHeight": NotRequired[str]
        }
    )

    ThemeHeadingsSizesH3 = TypedDict(
        "ThemeHeadingsSizesH3",
            {
            "fontSize": NotRequired[str],
            "fontWeight": NotRequired[str],
            "lineHeight": NotRequired[str]
        }
    )

    ThemeHeadingsSizesH4 = TypedDict(
        "ThemeHeadingsSizesH4",
            {
            "fontSize": NotRequired[str],
            "fontWeight": NotRequired[str],
            "lineHeight": NotRequired[str]
        }
    )

    ThemeHeadingsSizesH5 = TypedDict(
        "ThemeHeadingsSizesH5",
            {
            "fontSize": NotRequired[str],
            "fontWeight": NotRequired[str],
            "lineHeight": NotRequired[str]
        }
    )

    ThemeHeadingsSizesH6 = TypedDict(
        "ThemeHeadingsSizesH6",
            {
            "fontSize": NotRequired[str],
            "fontWeight": NotRequired[str],
            "lineHeight": NotRequired[str]
        }
    )

    ThemeHeadingsSizes = TypedDict(
        "ThemeHeadingsSizes",
            {
            "h1": NotRequired["ThemeHeadingsSizesH1"],
            "h2": NotRequired["ThemeHeadingsSizesH2"],
            "h3": NotRequired["ThemeHeadingsSizesH3"],
            "h4": NotRequired["ThemeHeadingsSizesH4"],
            "h5": NotRequired["ThemeHeadingsSizesH5"],
            "h6": NotRequired["ThemeHeadingsSizesH6"]
        }
    )

    ThemeHeadings = TypedDict(
        "ThemeHeadings",
            {
            "fontFamily": NotRequired[str],
            "fontWeight": NotRequired[str],
            "textWrap": NotRequired[Literal["wrap", "nowrap", "balance", "pretty", "stable"]],
            "sizes": NotRequired["ThemeHeadingsSizes"]
        }
    )

    ThemeRadius = TypedDict(
        "ThemeRadius",
            {
            "xs": NotRequired[str],
            "sm": NotRequired[str],
            "md": NotRequired[str],
            "lg": NotRequired[str],
            "xl": NotRequired[str]
        }
    )

    ThemeSpacing = TypedDict(
        "ThemeSpacing",
            {
            "xs": NotRequired[str],
            "sm": NotRequired[str],
            "md": NotRequired[str],
            "lg": NotRequired[str],
            "xl": NotRequired[str]
        }
    )

    ThemeFontSizes = TypedDict(
        "ThemeFontSizes",
            {
            "xs": NotRequired[str],
            "sm": NotRequired[str],
            "md": NotRequired[str],
            "lg": NotRequired[str],
            "xl": NotRequired[str]
        }
    )

    ThemeLineHeights = TypedDict(
        "ThemeLineHeights",
            {
            "xs": NotRequired[str],
            "sm": NotRequired[str],
            "md": NotRequired[str],
            "lg": NotRequired[str],
            "xl": NotRequired[str]
        }
    )

    ThemeBreakpoints = TypedDict(
        "ThemeBreakpoints",
            {
            "xs": NotRequired[str],
            "sm": NotRequired[str],
            "md": NotRequired[str],
            "lg": NotRequired[str],
            "xl": NotRequired[str]
        }
    )

    ThemeShadows = TypedDict(
        "ThemeShadows",
            {
            "xs": NotRequired[str],
            "sm": NotRequired[str],
            "md": NotRequired[str],
            "lg": NotRequired[str],
            "xl": NotRequired[str]
        }
    )

    ThemeDefaultGradient = TypedDict(
        "ThemeDefaultGradient",
            {
            "from": NotRequired[str],
            "to": NotRequired[str],
            "deg": NotRequired[NumberType]
        }
    )

    ThemeComponents = TypedDict(
        "ThemeComponents",
            {

        }
    )

    ThemeOther = TypedDict(
        "ThemeOther",
            {

        }
    )

    Theme = TypedDict(
        "Theme",
            {
            "focusRing": NotRequired[Literal["auto", "always", "never"]],
            "scale": NotRequired[NumberType],
            "fontSmoothing": NotRequired[bool],
            "white": NotRequired[str],
            "black": NotRequired[str],
            "colors": NotRequired["ThemeColors"],
            "primaryShade": NotRequired[typing.Union[Literal[2], Literal[1], Literal[3], Literal[4], Literal[5], Literal[6], Literal[7], Literal[8], Literal[9]]],
            "primaryColor": NotRequired[str],
            "variantColorResolver": NotRequired["ThemeVariantColorResolver"],
            "autoContrast": NotRequired[bool],
            "luminanceThreshold": NotRequired[NumberType],
            "fontFamily": NotRequired[str],
            "fontFamilyMonospace": NotRequired[str],
            "headings": NotRequired["ThemeHeadings"],
            "radius": NotRequired["ThemeRadius"],
            "defaultRadius": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "spacing": NotRequired["ThemeSpacing"],
            "fontSizes": NotRequired["ThemeFontSizes"],
            "lineHeights": NotRequired["ThemeLineHeights"],
            "breakpoints": NotRequired["ThemeBreakpoints"],
            "shadows": NotRequired["ThemeShadows"],
            "respectReducedMotion": NotRequired[bool],
            "cursorType": NotRequired[Literal["default", "pointer"]],
            "defaultGradient": NotRequired["ThemeDefaultGradient"],
            "activeClassName": NotRequired[str],
            "focusClassName": NotRequired[str],
            "components": NotRequired["ThemeComponents"],
            "other": NotRequired["ThemeOther"]
        }
    )

    ColorSchemeManager = TypedDict(
        "ColorSchemeManager",
            {
            "get": typing.Any,
            "set": typing.Any,
            "subscribe": typing.Any,
            "unsubscribe": typing.Any,
            "clear": typing.Any
        }
    )

    CssVariablesResolver = TypedDict(
        "CssVariablesResolver",
            {

        }
    )

    StylesTransform = TypedDict(
        "StylesTransform",
            {
            "sx": NotRequired[typing.Any],
            "styles": NotRequired[typing.Any]
        }
    )


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        theme: typing.Optional["Theme"] = None,
        colorSchemeManager: typing.Optional["ColorSchemeManager"] = None,
        defaultColorScheme: typing.Optional[Literal["auto", "dark", "light"]] = None,
        forceColorScheme: typing.Optional[Literal["dark", "light"]] = None,
        cssVariablesSelector: typing.Optional[str] = None,
        withCssVariables: typing.Optional[bool] = None,
        deduplicateCssVariables: typing.Optional[bool] = None,
        getRootElement: typing.Optional[typing.Any] = None,
        classNamesPrefix: typing.Optional[str] = None,
        getStyleNonce: typing.Optional[typing.Any] = None,
        cssVariablesResolver: typing.Optional["CssVariablesResolver"] = None,
        withStaticClasses: typing.Optional[bool] = None,
        withGlobalClasses: typing.Optional[bool] = None,
        stylesTransform: typing.Optional["StylesTransform"] = None,
        env: typing.Optional[Literal["default", "test"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'classNamesPrefix', 'colorSchemeManager', 'cssVariablesResolver', 'cssVariablesSelector', 'deduplicateCssVariables', 'defaultColorScheme', 'env', 'forceColorScheme', 'stylesTransform', 'theme', 'withCssVariables', 'withGlobalClasses', 'withStaticClasses']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'classNamesPrefix', 'colorSchemeManager', 'cssVariablesResolver', 'cssVariablesSelector', 'deduplicateCssVariables', 'defaultColorScheme', 'env', 'forceColorScheme', 'stylesTransform', 'theme', 'withCssVariables', 'withGlobalClasses', 'withStaticClasses']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MantineProvider, self).__init__(children=children, **args)

setattr(MantineProvider, "__init__", _explicitize_args(MantineProvider.__init__))
