# Official-library

Official build and addon library for [RocketBlend](https://github.com/rocketblend/rocketblend)

## How to use

To use one of the packages from this repository in your project, run the following command:

```bash
rocketblend install <package>
```

For example, to install Blender 3.6.21, run:

```bash
rocketblend install blender/3.6.21
```

See the [RocketBlend documentation](https://docs.rocketblend.io/getting-started/quick-start) for more information.

## Aliases

By default, packages from this repository are aliased so can be refered by their shorten references:

- `builds` = `github.com/rocketblend/official-library/packages/v0/builds`
- `addons` = `github.com/rocketblend/official-library/packages/v0/addons`
- `blender` = `github.com/rocketblend/official-library/packages/v0/builds/blender`

Therefore, the following references are all equivalent:
- `github.com/rocketblend/official-library/packages/v0/builds/blender/3.6.21`
- `builds/blender/3.6.21`
- `blender/3.6.21`

## Example Builds

* `blender/2.93.18` - LTS
* `blender/3.1.2`
* `blender/3.2.2`
* `blender/3.3.21` - LTS
* `blender/3.4.1`
* `blender/3.5.1`
* `blender/3.6.21` - LTS
* `blender/4.0.2`
* `blender/4.1.1`
* `blender/4.2.7` - LTS
* `blender/4.3.2`

## Tools

All build packages are generated using [Collector](https://github.com/rocketblend/rocketblend-collector)